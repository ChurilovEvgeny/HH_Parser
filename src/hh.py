from http import HTTPStatus

import requests

from src.parser import Parser
from src.vacancy import VacanciesList, Vacancy


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    # def __init__(self, file_worker):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = VacanciesList()
        # super().__init__(file_worker)

    def load_vacancies(self, keyword, salary: int, number_of_vacation: int):
        self.__params['text'] = " ".join(keyword)
        while number_of_vacation:
            # На одной странице не может быть больше 100 вакансий согласно API
            if number_of_vacation <= 100:
                per_page = number_of_vacation
                number_of_vacation = 0
            else:
                per_page = 100
                number_of_vacation -= 100
            self.__params['per_page'] = per_page
            self.__params['currency'] = "rur" # так же сразу указываем перевод в рубли

            # Если указываем зарплату, то дополнительно указываем на вывод вакансий ТОЛЬКО с зарплатами
            if salary:
                self.__params['salary'] = salary
                self.__params['only_with_salary'] = True

            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != HTTPStatus.OK:
                break

            resp_json = response.json()
            if 'items' not in resp_json:
                break

            vac_json = response.json()['items']
            [self.__vacancies.append(Vacancy(**vac)) for vac in vac_json]

            self.__params['page'] += 1

    @property
    def vacancies(self) -> VacanciesList:
        return self.__vacancies
