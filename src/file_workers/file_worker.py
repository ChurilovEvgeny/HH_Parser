import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy, VacanciesList


class FileWorker(ABC):
    _filename = ""

    def __init__(self, custom_filename: str | None = None):
        if custom_filename:
            self._filename = custom_filename

    @abstractmethod
    def load_all_from_file(self) -> VacanciesList:
        pass

    @abstractmethod
    def load_filtered_from_file(self, keywords: list[str]) -> VacanciesList:
        pass

    @abstractmethod
    def save_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        pass

    @abstractmethod
    def append_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_keywords(self, keywords: list[str]) -> list[Vacancy]:
        pass

    @abstractmethod
    def remove_vacancies_by_ids(self, vacancies_id: list[int]):
        pass

    def remove_file(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def _write_str_in_file(self, json_str):
        with open(self._filename, "w", encoding="utf-8") as f:
            f.write(json_str)
