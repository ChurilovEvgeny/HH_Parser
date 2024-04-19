import builtins

from src.user_interface import UserInterface


def test_user_interface_test_1(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python", "100", "15", "н"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface()
    ui.run_user_interface()
    out, _ = capsys.readouterr()
    assert out == "Добро пожаловать в программу поиска вакансий в HH.ru\nДо свидания!\n"
    assert ui.filter_words == ["Python"]
    assert ui.salary == 100
    assert ui.vacations_count == 15


def test_user_interface_test_2(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python", "text", "0", "text", "0", "3", "д",
                   "Java", "100", "15", "А", "н"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface()
    ui.run_user_interface()
    out, _ = capsys.readouterr()
    assert out == "Добро пожаловать в программу поиска вакансий в HH.ru\nДо свидания!\n"
    assert ui.filter_words == ["Java"]
    assert ui.salary == 100
    assert ui.vacations_count == 15
