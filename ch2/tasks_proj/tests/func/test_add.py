"""Проверить функцию API tasks.add ()."""
import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id():
    """tasks.add(valid task) добавление новой задачи
    должно возвращать целое число."""
    # когда новая задача добавлена
    # возвращается task_id типа int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_as_id_set():
    """Убедимся, что поле task_id установлено
    после применения метода tasks.add()."""
    # создаем новую задачу
    new_task = Task('sit in chair', owner='me', done=True)
    # добавляем новую задачу
    task_id = tasks.add(new_task)
    # получить задачу из БД по id
    task_from_db = tasks.get(task_id)
    # проверка на соответствие id созданной и полученной из БД задач
    assert task_from_db.id == task_id


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    ""




