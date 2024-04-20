from src.file_workers.JSON_worker import JSONWorker
from src.vacancy import Vacancy


def test_load_all_from_file():
    work = JSONWorker("test.json")
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 3
    assert vacancies.root[0].name == "Python"
    assert vacancies.root[1].name == "Java"
    assert vacancies.root[2].name == "C++"

    work = JSONWorker("nnt_exist.json")
    vacancies = work.load_all_from_file()
    assert vacancies.root is None


def test_get_vacancies_by_keywords():
    work = JSONWorker("test.json")
    vacancies = work.get_vacancies_by_keywords(["python", "java"])
    assert len(vacancies.root) == 2
    assert vacancies.root[0].name == "Python"
    assert vacancies.root[1].name == "Java"


def test_save_and_add_vacancies_to_json(get_valid_vacancy):
    work = JSONWorker("test.json")
    vacancies = work.load_all_from_file()

    work = JSONWorker("test_w.json")
    work.save_vacancies(vacancies)
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 3

    vac1 = Vacancy(**get_valid_vacancy)
    work.add_vacancy(vac1)
    vacancies = work.load_all_from_file()
    assert len(vacancies.root) == 4

    work.remove_file()
