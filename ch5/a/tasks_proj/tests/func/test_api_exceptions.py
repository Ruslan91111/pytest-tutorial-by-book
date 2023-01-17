"""Проверка ожидаемых исключений из использования API wrong."""
import pytest
import tasks
from tasks import Task

@pytest.mark.usefixtures('tasks_db')
class TestAdd():
    """Тесты, связанные с tasks.add()."""

    def test_missing_summary(self):
        """Следует поднять исключение, если summary missing."""
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))

    def test_done_not_bool(self):
        """Должно вызвать исключение, если done не является bool."""
        with pytest.raises(ValueError):
            tasks.add(Task(summary='summary', done='True'))