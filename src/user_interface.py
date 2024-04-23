from enum import Enum

from src.file_workers.file_worker import FileWorker
from src.parsers.parser import Parser


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
        self.parser: Parser = parser
        self.file_worker: FileWorker = file_worker

    def run_user_interface(self):
        self.__greetings()
        while True:
            match self.__select_function_main():
                case UIFunction.EXIT:
                    self.__farewell()
                    break

                case UIFunction.WORK_WITH_FILE:
                    self.__file_interface()

                case UIFunction.WORD_WITH_HH:
                    self.__hh_interface()

    @staticmethod
    def __greetings():
        print("Добро пожаловать в программу поиска вакансий в HH.ru")

    def __file_interface(self):
        while True:
            match self.__select_function_file():
                case FileFunction.EXIT:
                    return

                case FileFunction.OPEN_ALL:
                    print(self.file_worker.load_all_from_file())

                case FileFunction.OPEN_FILTERED:
                    self.__filter_words = self.__get_search_key_words()
                    print(self.file_worker.load_filtered_from_file(self.__filter_words))

                case FileFunction.REMOVE_BY_ID:
                    vac_ids = self.__get_vacancies_ids()
                    self.file_worker.remove_vacancies_by_ids(vac_ids)
                    self.__saved()

    def __hh_interface(self):
        while True:
            filter_words = self.__get_search_key_words()
            salary = self.__get_salary()
            vacations_count = self.__get_number_of_vacations()
            # Поиск и вывод
            self.parser.load_vacancies(filter_words, salary, vacations_count)
            print(self.parser.vacancies)

            match self.__select_function_hh():
                case HHFunction.EXIT:
                    return

                case HHFunction.NEW_SEARCH:
                    pass

                case HHFunction.SAVE_ALL:
                    self.file_worker.save_vacancies(self.parser.vacancies)
                    self.__saved()

                case HHFunction.SAVE_BY_ID:
                    vac_ids = self.__get_vacancies_ids()
                    self.file_worker.save_vacancies(self.parser.vacancies, vac_ids)
                    self.__saved()

                case HHFunction.APPEND_ALL:
                    self.file_worker.append_vacancies(self.parser.vacancies)
                    self.__saved()

                case HHFunction.APPEND_BY_ID:
                    vac_ids = self.__get_vacancies_ids()
                    self.file_worker.append_vacancies(self.parser.vacancies, vac_ids)
                    self.__saved()

    @staticmethod
    def __saved():
        print("Сохранено...")

    @staticmethod
    def __select_function_main() -> UIFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Работа с файлами;")
            print("2 - Работа с hh.ru;")
            print("0 - Выход;")

            ui = input("Номер функции: ").strip()
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 3:
                    return UIFunction(ui)

    @staticmethod
    def __select_function_file() -> FileFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Открыть файл целиком;")
            print("2 - Открыть отфильтрованный файл;")
            print("3 - Удалить выбранные id;")
            print("0 - Выход;")

            ui = input("Номер функции: ").strip()
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 4:
                    return FileFunction(ui)

    @staticmethod
    def __select_function_hh() -> HHFunction:
        while True:
            print("Выберете функцию:")
            print("1 - Новый поиск;")
            print("2 - Сохранить в файл всё;")
            print("3 - Сохранить выбранные id;")
            print("4 - Добавить в файл всё;")
            print("5 - Добавить выбранные id;")
            print("0 - Выход;")

            ui = input("Номер функции: ").strip()
            if ui.isdigit():
                ui = int(ui)
                if 0 <= ui < 6:
                    return HHFunction(ui)

    @staticmethod
    def __get_vacancies_ids() -> list[int]:
        while True:
            ids_list = input(
                "Введите сохраняемые id (разделенные пробелом): ").split()
            if ids_list and all(c.isdigit() for c in ids_list):
                return [int(c) for c in ids_list]

    @staticmethod
    def __get_search_key_words() -> list[str]:
        return input("Введите ключевые слова для фильтрации вакансий (разделенные пробелом): ").split()

    @staticmethod
    def __get_salary() -> int:
        while True:
            salary = input("Введите зарплату: (целые положительные числа; 0, если неважно) ")
            if salary.isdigit():
                salary = int(salary)
                if salary >= 0:
                    return salary

    @staticmethod
    def __get_number_of_vacations() -> int:
        while True:
            vac_count = input("Введите валидное количество вакансий для вывода в топ N (целые числа больше 0): ")
            if vac_count.isdigit():
                vac_count = int(vac_count)
                if vac_count > 0:
                    return vac_count

    @staticmethod
    def __farewell():
        print("До свидания!")
