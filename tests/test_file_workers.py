from src.file_workers.JSON_worker import JSONWorker
from src.vacancy import Vacancy


def test_load_all_from_file():
    work = JSONWorker("test.json")
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 4
    assert vacancies.root[0].name == "Стажер it специалист"
    assert vacancies.root[1].name == "Front-End Developer"
    assert vacancies.root[2].name == "Junior Golang Developer"

    work = JSONWorker("not_exist.json")
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 0


def test_load_filtered_from_file():
    work = JSONWorker("test.json")
    vacancies = work.load_filtered_from_file(["Стажер", "Golang"])
    assert len(vacancies.root) == 2
    assert vacancies.root[0].name == "Стажер it специалист"
    assert vacancies.root[1].name == "Junior Golang Developer"


def test_save_and_add_vacancies_to_json(get_valid_vacancy):
    work = JSONWorker("test.json")
    vacancies = work.load_all_from_file()

    work = JSONWorker("test_w.json")
    work.save_vacancies(vacancies)
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 4

    vac1 = Vacancy(**get_valid_vacancy)
    work.add_vacancy(vac1)
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 5

    vac_go_lang = work.load_filtered_from_file(["Golang"])
    assert len(vac_go_lang.root) == 1

    work.remove_vacancies_by_ids([96194079])
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 4

    work.append_vacancies(vac_go_lang, [96194079])
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 5

    work.remove_file()
