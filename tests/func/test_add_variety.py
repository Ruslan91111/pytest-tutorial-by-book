import pytest
import tasks
from tasks import Task


def test_add_1():
    """tasks.get () использует id, возвращаемый из add() works."""
    task = Task('breath', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # Все кроме идентификатора д.б. одинаковым
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Проверяет эквивалентность двух задач."""
    # Сравнить все, кроме поля id
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner)and
            (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Подключает к БД перед тестированием, отключает после."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()






