import builtins

from src.user_interface import UserInterface, HHFunction, FileFunction, UIFunction


def test_user_interface__get_number_of_vacations(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python", "0", "15"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__get_number_of_vacations()
    assert result == 15


def test_user_interface__get_salary(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__get_salary()
    assert result == 0


def test_user_interface__get_search_key_words(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python Java"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__get_search_key_words()
    assert result[0] == "Python"
    assert result[1] == "Java"


def test_user_interface__get_vacancies_ids(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["Python 15", "", "15 16"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__get_vacancies_ids()
    assert result[0] == 15
    assert result[1] == 16


def test_user_interface__select_function_hh(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["N", "-1", "6", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__select_function_hh()
    assert result == HHFunction.EXIT

    inputs = iter(["5"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = ui._UserInterface__select_function_hh()
    assert result == HHFunction.APPEND_BY_ID


def test_user_interface__select_function_file(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["N", "-1", "4", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__select_function_file()
    assert result == FileFunction.EXIT

    inputs = iter(["3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = ui._UserInterface__select_function_file()
    assert result == FileFunction.REMOVE_BY_ID


def test_user_interface__select_function_main(monkeypatch, capsys):
    # Список всей последовательности ввода в консоль
    inputs = iter(["N", "-1", "3", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    ui = UserInterface(None, None)
    result = ui._UserInterface__select_function_main()
    assert result == UIFunction.EXIT

    inputs = iter(["2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = ui._UserInterface__select_function_main()
    assert result == UIFunction.WORD_WITH_HH
