"""Содержит фикстуры общие для всех тестов приложения Tasks"""

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



