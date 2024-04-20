from typing import Self

from pydantic import BaseModel, RootModel, AnyHttpUrl, NonNegativeInt


class Vacancy(BaseModel):
    name: str
    url: AnyHttpUrl
    salary: NonNegativeInt
    region: str
    description: str

    def __str__(self):
        return (f"{30 * '*'}\n"
                f"Вакансия: {self.name}\n"
                f"URL: {self.url}\n"
                f"Зарплата: {self.salary}\n"
                f"Регион: {self.region}\n\n"
                f"{self.description}")

    def __gt__(self, other: Self):
        self.__vacancy_type_validate(other)
        return self.salary > other.salary

    def __ge__(self, other: Self):
        self.__vacancy_type_validate(other)
        return self.salary >= other.salary

    def __eq__(self, other: Self):
        self.__vacancy_type_validate(other)
        return self.salary == other.salary

    @staticmethod
    def __vacancy_type_validate(instance):
        if not isinstance(instance, Vacancy):
            raise TypeError("Сравнивать можно только с типом Vacancy")


class VacanciesList(RootModel):
    root: list[Vacancy] = None

    def append(self, vacancy: Vacancy):
        if self.root is None:
            self.root = []

        self.root.append(vacancy)
