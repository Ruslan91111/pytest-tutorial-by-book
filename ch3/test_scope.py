""" Демонстрация параметра scope в действии"""
import pytest


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    """Тест с использованием сессий, модулей и функций."""


def test_2(sess_scope, mod_scope, func_scope):
    """Демонстрация более увлекательна со множеством тестов."""


@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""






