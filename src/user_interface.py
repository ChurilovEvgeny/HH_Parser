from enum import Enum

from src.file_workers.file_worker import FileWorker
from src.parser import Parser


class UIFunction(Enum):
    EXIT = 0
    WORK_WITH_FILE = 1
    WORD_WITH_HH = 2

class FileFunction(Enum):
    EXIT = 0
    OPEN_ALL = 1
    OPEN_FILTERED = 2
    REMOVE_BY_ID = 3

class HHFunction(Enum):
    EXIT = 0
    NEW_SEARCH = 1
    SAVE_ALL = 2
    SAVE_BY_ID = 3
    APPEND_ALL = 4
    APPEND_BY_ID = 5


class UserInterface:
    def __init__(self, parser: Parser, file_worker: FileWorker):
        self.__vacations_count: int = 1
        self.__filter_words: list[str] = []
        self.__salary: int = 0

        self.parser: Parser = parser
        self.file_worker: FileWorker = file_worker

    @property
    def vacations_count(self):
        return self.__vacations_count

    @property
    def filter_words(self):
        # Возвращаем копию списка, чтобы нельзя было модифицировать приватное поле из вне
        return self.__filter_words[:]

    @property
    def salary(self):
        return self.__salary

    def run_user_interface(self):

        def file_interface():
            def get_vacancies_ids():
                while True:
                    ids_list = input(
                        "Введите сохраняемые id (разделенные пробелом): ").split()
                    if ids_list and all(c.isdigit() for c in ids_list):
                        return [int(c) for c in ids_list]

            while True:
                func = self.__select_function_file()
                match func:
                    case FileFunction.EXIT:
                        return

                    case FileFunction.OPEN_ALL:
                        print(self.file_worker.load_all_from_file())

                    case FileFunction.OPEN_FILTERED:
                        self.__get_search_key_words()
                        print(self.file_worker.load_filtered_from_file(self.__filter_words))

                    case FileFunction.REMOVE_BY_ID:
                        vac_ids = get_vacancies_ids()
                        self.file_worker.remove_vacancies_by_ids(vac_ids)
                        self.__saved()

        def hh_interface():
            def get_vacancies_ids():
                while True:
                    ids_list = input(
                        "Введите сохраняемые id (разделенные пробелом): ").split()
                    if ids_list and all(c.isdigit() for c in ids_list):
                        return [int(c) for c in ids_list]

            while True:
                self.__get_search_key_words()
                self.__get_salary()
                self.__get_number_of_vacations()
                # Поиск и вывод
                self.parser.load_vacancies(self.filter_words, self.salary, self.vacations_count)
                print(self.parser.vacancies)

                func = self.__select_function_hh()
                match func:
                    case HHFunction.EXIT:
                        return

                    case HHFunction.NEW_SEARCH:
                        pass

                    case HHFunction.SAVE_ALL:
                        self.file_worker.save_vacancies(self.parser.vacancies)
                        self.__saved()

                    case HHFunction.SAVE_BY_ID:
                        vac_ids = get_vacancies_ids()
                        self.file_worker.save_vacancies(self.parser.vacancies, vac_ids)
                        self.__saved()

                    case HHFunction.APPEND_ALL:
                        self.file_worker.append_vacancies(self.parser.vacancies)
                        self.__saved()

                    case HHFunction.APPEND_BY_ID:
                        vac_ids = get_vacancies_ids()
                        self.file_worker.append_vacancies(self.parser.vacancies, vac_ids)
                        self.__saved()

        self.__greetings()
        while True:
            func = self.__select_function_main()
            match func:
                case UIFunction.EXIT:
                    self.__farewell()
                    break

                case UIFunction.WORK_WITH_FILE:
                    file_interface()

                case UIFunction.WORD_WITH_HH:
                    hh_interface()

            # if not self.__is_create_new_search_request():
            #     self.__farewell()
            #     break

    def __greetings(self):
        print("Добро пожаловать в программу поиска вакансий в HH.ru")

    def __saved(self):
        print("Сохранено...")

    def __select_function_main(self) -> UIFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Работа с файлами;")
            print("2 - Работа с hh.ru;")
            print("0 - Выход;")

            ui = input("Номер функции: ")
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 3:
                    return UIFunction(ui)

    def __select_function_file(self) -> FileFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Открыть файл целиком;")
            print("2 - Открыть отфильтрованный файл;")
            print("3 - Удалить выбранные id;")
            print("0 - Выход;")

            ui = input("Номер функции: ")
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 4:
                    return FileFunction(ui)

    def __select_function_hh(self) -> HHFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Новый поиск;")
            print("2 - Сохранить в файл всё;")
            print("3 - Сохранить выбранные id;")
            print("4 - Добавить в файл всё;")
            print("5 - Добавить выбранные id;")
            print("0 - Выход;")

            ui = input("Номер функции: ")
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 6:
                    return HHFunction(ui)

    def __get_search_key_words(self):
        self.__filter_words = input("Введите ключевые слова для фильтрации вакансий (разделенные пробелом): ").split()

    def __get_salary(self):
        while True:
            salary = input("Введите зарплату: (целые положительные числа; 0, если неважно) ")
            if salary.isdigit():
                salary = int(salary)
                if salary >= 0:
                    self.__salary = salary
                    break

    def __get_number_of_vacations(self):
        while True:
            vac_count = input("Введите валидное количество вакансий для вывода в топ N (целые числа больше 0): ")
            if vac_count.isdigit():
                vac_count = int(vac_count)
                if vac_count > 0:
                    self.__vacations_count = vac_count
                    break

    def __is_create_new_search_request(self):
        while True:
            user_answer = input("Хотите сформировать новый запрос? [д/н]: ").lower()
            if user_answer == "д":
                return True
            elif user_answer == "н":
                return False

    def __farewell(self):
        print("До свидания!")
