from src.file_workers.file_worker import FileWorker
from src.vacancy import Vacancy, VacanciesList


class JSONWorker(FileWorker):
    _filename = "data.json"

    def __init__(self, custom_filename: str | None = None):
        super().__init__(custom_filename)

    def load_all_from_file(self) -> VacanciesList:
        try:
            vac = VacanciesList.parse_file(self._filename)
        except FileNotFoundError:
            vac = VacanciesList()
        return vac

    def load_filtered_from_file(self, keywords: list[str]) -> VacanciesList:
        vacancies = self.load_all_from_file()
        vacancies.filter_vacancies_by_keyword(keywords)
        return vacancies

    def save_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        vacancies.filter_vacancies_by_ids(vacancies_id)
        json_str = vacancies.model_dump_json(indent=2)
        self._write_str_in_file(json_str)

    def append_vacancies(self, vacancies: VacanciesList, vacancies_id: list[int] | None = None):
        vacancies.filter_vacancies_by_ids(vacancies_id)
        vacancies_from_file = self.load_all_from_file()
        [vacancies.append(v) for v in vacancies_from_file.root]
        self.save_vacancies(vacancies)

    def add_vacancy(self, vacancy: Vacancy):
        vacancies = self.load_all_from_file()
        vacancies.append(vacancy)
        self.save_vacancies(vacancies)

    def get_vacancies_by_keywords(self, keywords: list[str]) -> VacanciesList:
        vacancies = self.load_all_from_file()

        res_vacancies = VacanciesList()
        for _, items in vacancies:
            for vac in items:
                for key in keywords:
                    if key.lower().strip() in vac.name.lower():
                        res_vacancies.append(vac)

        return res_vacancies

    def remove_vacancies_by_ids(self, vacancies_id: list[int]):
        vacancies_from_file = self.load_all_from_file()
        vacancies_from_file.remove_vacancies_by_ids(vacancies_id)
        json_str = vacancies_from_file.model_dump_json(indent=2)
        self._write_str_in_file(json_str)
