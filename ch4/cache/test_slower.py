"""Фикстура для фиксации времени тестов."""
import datetime
import random
import time

import pytest


# Поскольку фикстура autouse-используется для всего теста.
# Объект request используется для получения nodeid что бы использовать в ключе.
# "nodeid" — уникальный идентификатор, который работает даже с параметризованными тестами.
# Мы добавляем ключ с 'duration/', чтобы быть добропорядочныи жителями кэша.
# Код до yield - до тестовой функции; код после yield - после тестовой функции.
@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeit.replace(':', '_')
    # идентификатор узла (nodeid) может иметь двоеточия
    # ключи становятся именами файлов внутри .cache
    # меняем двоеточия на что-то безопасное в имени файла
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = "длительность теста превышает последний более, чем в 2 раза"
        assert this_duration <= last_duration * 2, errorstring


# Чтобы не писать кучу тестов используем random и параметризацию,
# чтобы cгенерить некоторые тесты, которые поспят в течение случайного
# количества времени, все короче секунды.
@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())

