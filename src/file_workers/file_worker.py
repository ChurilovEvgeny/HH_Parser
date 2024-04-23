import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy, VacanciesList


class FileWorker(ABC):
    _filename = ""

    def __init__(self, custom_filename: str | None = None):
        if custom_filename:
            self._filename = custom_filename

    @abstractmethod
    def save_vacancies(self, vacancies: VacanciesList):
        pass

    @abstractmethod
    def append_vacancies(self, vacancies: VacanciesList):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_keywords(self, keywords: list[str]) -> list[Vacancy]:
        pass

    @abstractmethod
    def remove_vacancy_by_id(self, vacancy_id: int):
        pass

    def remove_file(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def _append_str_in_file(self, json_str):
        with open(self._filename, "w", encoding="utf-8") as f:
            f.write(json_str)
