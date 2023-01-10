from collections import namedtuple


# создаем именованный кортеж с названием Task и полями: summary и т.д.
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])

# __new __.__ defaults__ для создания объектов Task без указания всех полей.
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """
    Без использования параметров, следует ссылаться на значения по умолчанию.
    Тест предназначен для демонстрации и проверки того, как работают умолчания
    """
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Проверка свойства .field (поля) namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)



