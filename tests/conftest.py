import pytest


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
