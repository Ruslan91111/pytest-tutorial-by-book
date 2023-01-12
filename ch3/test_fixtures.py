import pytest


@pytest.fixture()
def some_data():
    """ Функция просто возвращает число"""
    return 42


def test_some_data(some_data):
    """ Проверить возвращает ли функция some_data число 42"""
    assert some_data == 42


@pytest.fixture()
def a_tuple():
    """Вернуть кортеж смешанного типа"""
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]['bar'] == 32



