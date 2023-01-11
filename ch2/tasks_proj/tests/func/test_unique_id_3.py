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


@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Вызов unique_id () дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() должен вернуть неиспользуемый id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # захват уникального id
    uid = tasks.unique_id()
    # убеждаемся, что его нет в списке существующих идентификаторов
    assert uid not in ids
