from pydantic import PositiveInt

from src.file_workers.JSON_worker import JSONWorker
from src.hh import HH
from src.user_interface import UserInterface
from src.vacancy import Vacancy

# import requests
# url = 'https://api.hh.ru/vacancies'
# headers = {'User-Agent': 'HH-User-Agent'}
# params = {'text': 'Python', 'page': 0, 'per_page': 3,}
# resp = requests.get(url=url, headers=headers, params=params)
# print(resp.text)


if __name__ == "__main__":
    UserInterface(HH()).run_user_interface()
    #  dat = {
    #      'name': 'Имя',
    #      'url': 'https://hh.ru',
    #      'salary': 50000,
    #      'region': 'СПБ',
    #      'description': 'Текст описания',
    #  }
    #  Vacancy(**dat)