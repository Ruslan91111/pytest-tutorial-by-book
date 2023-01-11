import pytest


@pytest.fixture()
def some_data():
    """ Функция просто возвращает число"""
    return 42


def test_some_data(some_data):
    """ Проверить возвращает ли функция some_data число 42"""
    assert some_data == 42



