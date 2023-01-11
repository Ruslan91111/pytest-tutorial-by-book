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



