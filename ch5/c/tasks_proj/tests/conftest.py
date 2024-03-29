"""
Определить фикстуры для использования в проекте.
В этом файле также настраиваем отображение в терминале сообщений о падении теста.
При помощи опции --nice
"""


import pytest
import tasks
from tasks import Task


# область сеанса
# @pytest.fixture(scope='session', params=['tiny',])
@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory, request):
    """ Подключение к БД один раз перед тестами, отключение после."""
    # создать временный каталог
    temp_dir = tmpdir_factory.mktemp('temp')
    # поключиться к временной БД
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield # выполнение тестовых функций

    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """Очистить БД"""
    tasks.delete_all()


# Фикстура с данными (тремя разными).
@pytest.fixture()
def tasks_just_a_few():
    """Все задачи и исполнители уникальны."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


# Фикстура с данными: задачами, распределенными по несколько на одного исполнителя.
@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """Несколько исполнителей с несколькими задачами каждый."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """ Подключение БД с 3 задачами, все уникальны."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_multi_per_owner):
    """ Подключение БД с 9 задачами, 3 исполнителями, по три на каждого."""
    for t in tasks_multi_per_owner:
        tasks.add(t)


# Функция - хук для вывода ободряющего сообщения
# def pytest_report_header():
#     return "Thanks for running the test."

# # функция - хук для вывода 'O' вместо 'F'
# def pytest_report_teststatus(report):
#     if report.when == 'call' and report.failed:
#             return (report.outcome, 'O', 'OPPORTUNITY for improvement')



# Добавление параметра командной строки, "--nice", чтобы изменения статуса
# происходили, только если подставить --nice.
def pytest_addoption(parser):
    """Включает nice функцию с опцией --nice."""
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
                    help="nice: turn failures into opportunities")


def pytest_report_header(config):
    """Благодарность тестеру за выполнение тестов."""
    if config.getoption('nice'):
        return "Thanks for running the tests."


def pytest_report_teststatus(report, config):
    """Превращает неудачи в возможности."""
    if report.when == 'call':
        if report.failed and config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')




