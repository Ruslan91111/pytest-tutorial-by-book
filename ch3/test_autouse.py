"""Демонстрация работы параметра autouse, но лучше использовать
Фикстуры как декораторы"""

import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Сообщает время в конце session(сеанса)."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d, %b, %x', time.localtime(now))))
    print('---------------')


@pytest.fixture(autouse=True)
def footer_functiion_scope():
    """Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1():
    """Имитирует длительный тестовый тест."""
    time.sleep(1)

def test_2():
    """Имитирует еще более длительный тест"""
    time.sleep(1.23)

