"""Проверить функцию API tasks.add ()."""
import pytest
import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) должен возвращать целое число."""
    # когда новая задача добавлена
    # возвращается task_id типа int
    # GIVEN - ДАНО
    new_task = Task('do something')
    # WHEN - КОГДА
    task_id = tasks.add(new_task)
    # THEN - ПОСЛЕ
    assert isinstance(task_id, int)


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() должен повлиять на tasks.count()."""
    # GIVEN - db с 3 задачами
    # WHEN - добавляется ещё одна задача
    tasks.add(Task('throw a party'))

    # THEN - счетчик увеличивается на 1
    assert tasks.count() == 4



