from src.file_workers.file_worker import FileWorker
from src.vacancy import Vacancy, VacanciesList


class JSONWorker(FileWorker):
    _filename = "data.json"

    def __init__(self, custom_filename: str | None = None):
        super().__init__(custom_filename)

    def load_all_from_file(self) -> VacanciesList:
        """
        Загружает все вакансии из файла
        :return: список вакансий
        """
        try:
            vac = VacanciesList.parse_file(self._filename)
        except FileNotFoundError:
            vac = VacanciesList()
        return vac

    def load_filtered_from_file(self, keywords: list[str]) -> VacanciesList:
        """
        Загружает вакансии, которые соответствую заданным ключам.
        Ключи работают по ИЛИ
        :param keywords: список ключей
        :return: список вакансий
        """
        vacancies = self.load_all_from_file()
        vacancies.filter_vacancies_by_keyword(keywords)
        return vacancies

    def save_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        """
        Сохраняет в файл (перезаписывает) вакансии. Если задан список id вакансий, то сохраняет только с заданными id
        :param vacancies: список вакансий VacanciesList
        :param vacancies_id: список id сохраняемых вакансий. Если не задан, то сохраняются все
        :return: None
        """
        vacancies.filter_vacancies_by_ids(vacancies_id)
        json_str = vacancies.model_dump_json(indent=2)
        self._write_str_in_file(json_str)

    def append_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        """
        Добавляет в файл вакансии. Если задан список id вакансий, то добавляет только с заданными id
        :param vacancies: список вакансий VacanciesList
        :param vacancies_id: список id добавляемых вакансий. Если не задан, то добавляются все
        :return: None
        """
        vacancies.filter_vacancies_by_ids(vacancies_id)
        vacancies_from_file = self.load_all_from_file()
        [vacancies.append(v) for v in vacancies_from_file.root]
        self.save_vacancies(vacancies)

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет одну вакансию в файл
        :param vacancy: добавляемая вакансия типа Vacancy
        :return: None
        """
        vacancies = self.load_all_from_file()
        vacancies.append(vacancy)
        self.save_vacancies(vacancies)

    def remove_vacancies_by_ids(self, vacancies_id: list[int]):
        """
        Удаляет из файла вакансии с соответствующими id
        :param vacancies_id: список удаляемых id
        :return: None
        """
        vacancies_from_file = self.load_all_from_file()
        vacancies_from_file.remove_vacancies_by_ids(vacancies_id)
        json_str = vacancies_from_file.model_dump_json(indent=2)
        self._write_str_in_file(json_str)
