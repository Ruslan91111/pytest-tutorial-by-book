    """Проверка на ожидаемые исключения из-за неправильного использования API."""

    import pytest
    import tasks

    def test_add_raises():
        """add() должно возникнуть исключение с неправильным типом param."""
        with pytest.raises(TypeError):
            tasks.add(task='not a Task object')