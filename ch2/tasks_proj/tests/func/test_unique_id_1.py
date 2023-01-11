import pytest
import tasks


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """
    Соединение с БД перед тестом, разрыв соединения после
    """
    # Setup | start db
    # Установка соединения с БД
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # здесь происходит тестирование

    # Teardown : stop db
    # разрыв соединения после тестирования
    tasks.stop_tasks_db()


def test_unique_id():
    """Вызов unique_id () дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

