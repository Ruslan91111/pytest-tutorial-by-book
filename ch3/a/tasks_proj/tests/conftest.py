""" """
import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """ Подключение к БД перед тестами, отключение после."""
    # setup
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    # teardown
    tasks.stop_tasks_db()


# фикстура с тремя разными разными данными
@pytest.fixture()
def tasks_just_a_few():
    """Все задачи и исполнители уникальны."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


# фикстура с данными: задачами, распределенными по несколько на одного исполнителя
@pytest.fixture()
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





    # Памятка об интерфейсе Task constructor
    # Task(summary=None, owner=None, done=False, id=None)
    # summary то что требуется
    # owner и done являются необязательными
    # id задается базой данных
