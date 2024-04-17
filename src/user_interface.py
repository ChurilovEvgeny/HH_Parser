class UserInterface():
    def __init__(self):
        self.vacations_count: int = 1
        self.filter_words: str = ""
        self.salary: int = 0

    def run_user_interface(self):
        self.__greetings()
        self.__get_search_key_words()
        self.__get_salary()
        self.__get_number_of_vacations()
        # Поиск и вывод

        if not self.__is_create_new_search_request():
            self.__farewell()

    def __greetings(self):
        print("Добро пожаловать в программу поиска вакансий в HH.ru")

    def __get_search_key_words(self):
        self.filter_words = input("Введите ключевые слова для фильтрации вакансий (разделенные пробелом): ").split()

    def __get_salary(self):
        while True:
            salary = input("Введите зарплату: (целые положительные числа; 0, если неважно)")
            if salary.isdigit():
                salary = int(salary)
                if salary >= 0:
                    self.salary = salary
                    break

    def __get_number_of_vacations(self):
        while True:
            vac_count = input("Введите валидное количество вакансий для вывода в топ N (целые числа больше 0): ")
            if vac_count.isdigit():
                vac_count = int(vac_count)
                if vac_count > 0:
                    self.vacations_count = vac_count
                    break

    def __is_create_new_search_request(self):
        while True:
            user_answer = input("Хотите сформировать новый запрос?: [д/н]").lower()
            if user_answer == "д":
                return True
            elif user_answer == "н":
                return False

    def __farewell(self):
        print("До свидания!")