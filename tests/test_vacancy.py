import pytest
from pydantic import ValidationError

from src.vacancy import Vacancy


@pytest.fixture
def get_valid_vacancy():
    return {
        'name': 'Имя',
        'url': 'https://hh.ru',
        'salary': 50000,
        'region': 'СПБ',
        'description': 'Текст описания',
    }


@pytest.fixture
def get_url_failed_vacancy():
    return {
        'name': 'Имя',
        'url': 'NONE',
        'salary': 0,
        'region': 'СПБ',
        'description': 'Текст описания',
    }


@pytest.fixture
def get_salary_failed_1_vacancy():
    return {
        'name': 'Имя',
        'url': 'https://hh.ru',
        'salary': "fgd",
        'region': 'СПБ',
        'description': 'Текст описания',
    }


@pytest.fixture()
def get_salary_failed_2_vacancy():
    return {
        'name': 'Имя',
        'url': 'https://hh.ru',
        'salary': -100,
        'region': 'СПБ',
        'description': 'Текст описания',
    }


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
