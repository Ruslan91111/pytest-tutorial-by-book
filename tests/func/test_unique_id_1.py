import pytest
import tasks


def test_unique_id():
    """Вызов unique_id() дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2






