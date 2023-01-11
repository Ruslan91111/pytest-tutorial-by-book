import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """
    Соединение с БД перед тестом, разрыв соединения после
    """
    # Setup | start db
    # Установка соединения с БД
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # здесь происходит тестирование
    # Teardown : stop db
    # разрыв соединения после тестирования
    tasks.stop_tasks_db()


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Вызов unique_id () дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Демонстрация xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Демонстрация xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'


def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # grab a unique id
    uid = tasks.unique_id()
    # make sure it isn't in the list of existing ids
    assert uid not in ids