import pytest
from pydantic import ValidationError

from src.vacancy import Vacancy, VacanciesList


def test_single_vacancy(get_valid_vacancy, capsys):
    vac = Vacancy(**get_valid_vacancy)
    assert vac.name == "Имя"
    assert vac.salary == 50000
    assert vac.region == "СПБ"
    assert vac.description == "Текст описания"
    print(vac)
    out = capsys.readouterr().out
    assert out == '******************************\nВакансия: Имя\nURL: https://hh.ru/\nЗарплата: 50000\nРегион: СПБ\n\nТекст описания\n'


def test_vacancy_validate_url(get_url_failed_vacancy):
    with pytest.raises(ValidationError):
        Vacancy(**get_url_failed_vacancy)


def test_vacancy_validate_name(get_salary_failed_1_vacancy, get_salary_failed_2_vacancy):
    with pytest.raises(ValidationError):
        Vacancy(**get_salary_failed_1_vacancy)

    with pytest.raises(ValidationError):
        Vacancy(**get_salary_failed_2_vacancy)


def test_comparison(get_valid_vacancy):
    vac1 = Vacancy(**get_valid_vacancy)
    vac2 = Vacancy(**get_valid_vacancy)
    vac3 = Vacancy(**get_valid_vacancy)
    vac2.salary = 60000
    vac3.salary = 60000
    assert vac2 > vac1
    assert vac2 >= vac1
    assert vac3 == vac2

    assert vac1 < vac2
    assert vac1 <= vac2
    assert vac1 != vac2

    with pytest.raises(TypeError):
        vac1 > 1000


def test_list_of_vavancies(get_valid_vacancy):
    vac1 = Vacancy(**get_valid_vacancy)
    vac2 = Vacancy(**get_valid_vacancy)
    vac_lst = VacanciesList(root=[vac1, vac2])
    assert len(vac_lst.root) == 2
