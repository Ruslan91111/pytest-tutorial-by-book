"""Фикстура для фиксации времени тестов."""
import datetime
import random
import time
from collections import namedtuple

import pytest


Duration = namedtuple('Duration', ['current', 'last'])


#Фикстура duration_cache принадлежит области сеанса. Она читает предыдущую запись или
# пустой словарь, если нет предыдущих кэшированных данных,
# прежде чем запускать какие-либо тесты
@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


# Сохраняем как извлеченный словарь, так и пустой в namedtuple именуемый Duration
# с методами доступа current и last. Затем мы передаем этот namedtuple в test_duration,
# который является функцией и запускается для каждой тестовой функции.
# По мере выполнения теста, то же namedtuple передается в каждый тест,
# и время для текущего теста хранятся в словарь d.current.
# По окончании тестового сеанса собранный текущий словарь сохраняется в кеше.
@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration
    if d.last.get(nodeid, None) is not None:
        errorstring = "длительность теста превышает последний более, чем в 2 раза"
        assert duration <= (d.last[nodeid] * 2), errorstring


# Чтобы не писать кучу тестов используем random и параметризацию,
# чтобы cгенерить некоторые тесты, которые поспят в течение случайного
# количества времени, все короче секунды.
@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())

