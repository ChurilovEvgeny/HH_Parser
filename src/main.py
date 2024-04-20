from pydantic import PositiveInt

from src.user_interface import UserInterface

# import requests
# url = 'https://api.hh.ru/vacancies'
# headers = {'User-Agent': 'HH-User-Agent'}
# params = {'text': 'Python', 'page': 0, 'per_page': 3,}
# resp = requests.get(url=url, headers=headers, params=params)
# print(resp.text)


if __name__ == "__main__":
    UserInterface().run_user_interface()
