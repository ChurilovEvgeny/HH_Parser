import pytest
from pydantic import ValidationError

from src.vacancy import Vacancy, VacanciesList


def test_single_vacancy(get_valid_vacancy, capsys):
    vac = Vacancy(**get_valid_vacancy)
    assert vac.id == 111
    assert vac.name == "Имя"
    assert str(vac.alternate_url) == 'https://hh.ru/'
    assert vac.salary is None
    assert vac.area["name"] == "СПБ"
    assert vac.schedule["name"] == "Полная занятость"
    print(vac)
    out = capsys.readouterr().out
    assert out == '******************************\nid: 111\nВакансия: Имя\nURL: https://hh.ru/\nЗарплата: Не указана\nРегион: СПБ\nГрафик: Полная занятость\n\n'


def test_single_vacancy_3(get_valid_vacancy_3, capsys):
    vac = Vacancy(**get_valid_vacancy_3)
    print(vac)
    out = capsys.readouterr().out
    assert out == '******************************\nid: 111\nВакансия: Имя\nURL: https://hh.ru/\nЗарплата: От 5000 rub до 6000 rub до вычета налогов\nРегион: Не указан\nГрафик: Не указан\n\n'


def test_vacancy_validate_url(get_url_failed_vacancy):
    with pytest.raises(ValidationError):
        Vacancy(**get_url_failed_vacancy)


def test_vacancy_validate_name(get_salary_failed_1_vacancy, get_salary_failed_2_vacancy):
    with pytest.raises(ValidationError):
        Vacancy(**get_salary_failed_1_vacancy)

    with pytest.raises(ValidationError):
        Vacancy(**get_salary_failed_2_vacancy)


def test_comparison(get_valid_vacancy_2):
    vac1 = Vacancy(**get_valid_vacancy_2)
    vac2 = Vacancy(**get_valid_vacancy_2)
    vac1.salary["from"] = 5000
    vac2.salary["from"] = 6000
    vac1.salary["to"] = 10000
    vac2.salary["to"] = 10000

    assert vac2 > vac1
    assert vac2 >= vac1
    assert vac2 != vac1

    assert vac1 < vac2
    assert vac1 <= vac2
    assert not vac1 == vac2

    vac1.salary["from"] = 5000
    vac2.salary["from"] = 5000
    vac1.salary["to"] = 10000
    vac2.salary["to"] = 11000

    assert vac1 < vac2
    assert vac1 <= vac2
    assert vac1 != vac2

    vac1.salary["from"] = 5000
    vac2.salary["from"] = 5000
    vac1.salary["to"] = 10000
    vac2.salary["to"] = 10000
    assert vac1 == vac2

    vac1.salary["from"] = 5000
    vac2.salary["from"] = 5000
    vac1.salary["to"] = None
    vac2.salary["to"] = 10000
    assert vac1 < vac2

    vac1.salary["from"] = 5000
    vac2.salary["from"] = 5000
    vac1.salary["to"] = None
    vac2.salary["to"] = None
    assert vac1 == vac2

    vac1.salary["from"] = None
    vac2.salary["from"] = None
    vac1.salary["to"] = 10000
    vac2.salary["to"] = 10000
    assert vac1 == vac2

    vac1.salary = None
    vac2.salary["from"] = 5000
    assert vac1 < vac2

    vac1.salary = None
    vac2.salary["from"] = 5000
    assert vac1 != vac2

    vac1.salary = None
    vac2.salary = None
    assert vac1 == vac2

    with pytest.raises(TypeError):
        vac1 > 1000


def test_list_of_vacancies(get_valid_vacancy):
    vac1 = Vacancy(**get_valid_vacancy)
    vac2 = Vacancy(**get_valid_vacancy)
    vac_lst = VacanciesList(root=[vac1, vac2])
    assert len(vac_lst.root) == 2

    vac2_lst = VacanciesList()
    assert vac2_lst.root is None
    vac2_lst.append(vac1)
    assert len(vac2_lst.root) == 1
    assert str(
        vac2_lst) == '******************************\nid: 111\nВакансия: Имя\nURL: https://hh.ru/\nЗарплата: Не указана\nРегион: СПБ\nГрафик: Полная занятость\n'
