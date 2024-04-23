import json

import pytest


@pytest.fixture
def get_valid_vacancy():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'https://hh.ru',
        'salary': None,
        'area': {'name': 'СПБ'},
        'schedule': {'name': 'Полная занятость'},
    }


@pytest.fixture
def get_valid_vacancy_2():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'https://hh.ru',
        'salary': {'from': 5000, 'to': 60000},
        'area': {'name': 'СПБ'},
        'schedule': {'name': 'Полная занятость'},
    }


@pytest.fixture
def get_valid_vacancy_3():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'https://hh.ru',
        'salary': {'from': 5000, 'to': 6000, 'currency': "rub", 'gross': True},
        'area': None,
        'schedule': None,
    }


@pytest.fixture
def get_url_failed_vacancy():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'None',
        'salary': None,
        'area': {'name': 'СПБ'},
        'schedule': {'name': 'Полная занятость'},
    }


@pytest.fixture
def get_salary_failed_1_vacancy():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'https://hh.ru',
        'salary': 111,
        'area': {'name': 'СПБ'},
        'schedule': {'name': 'Полная занятость'},
    }


@pytest.fixture()
def get_salary_failed_2_vacancy():
    return {
        'id': 111,
        'name': 'Имя',
        'alternate_url': 'https://hh.ru',
        'salary': "None",
        'area': {'name': 'СПБ'},
        'schedule': {'name': 'Полная занятость'},
    }


@pytest.fixture()
def get_program_languages_vacancies():
    return [
        {
            "name": "Python",
            "url": "https://hh.ru/",
            "salary": 50000,
            "region": "СПБ",
            "description": "Текст описания"
        },
        {
            "name": "Java",
            "url": "https://hh.ru/",
            "salary": 50000,
            "region": "СПБ",
            "description": "Текст описания"
        },
        {
            "name": "C++",
            "url": "https://hh.ru/",
            "salary": 50000,
            "region": "СПБ",
            "description": "Текст описания"
        }
    ]


@pytest.fixture
def get_response_page_0():
    with open("resp_page_0.json", "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def get_response_page_1():
    with open("resp_page_1.json", "r", encoding="utf-8") as f:
        return json.load(f)
