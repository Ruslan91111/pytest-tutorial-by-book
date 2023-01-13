"""Демонстрация переименования фикстуры"""

import pytest


@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    """Возвращает окончательный ответ."""
    return 42


def test_everything(lue):
    """Использует более короткое имя."""
    assert lue == 42

