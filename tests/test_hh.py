import responses

from src.parsers.hh import HH


@responses.activate
def test_load_vacancies(get_response_page_0, get_response_page_1):
    responses.add(responses.GET, 'https://api.hh.ru/vacancies', json=get_response_page_0, status=200)
    responses.add(responses.GET, 'https://api.hh.ru/vacancies', json=get_response_page_1, status=200)
    responses.add(responses.GET, 'https://api.hh.ru/vacancies', json={}, status=404)

    hh = HH()
    hh.load_vacancies(["Python"], 100, 201)
    vac_list = hh.vacancies
    assert len(vac_list.root) == 101

    responses.add(responses.GET, 'https://api.hh.ru/vacancies', json={}, status=200)
    hh = HH()
    hh.load_vacancies(["Python"], 100, 1)
    vac_list = hh.vacancies
    assert len(vac_list.root) == 0
