"""Проверка фукции API tasks.add()."""

import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """созадать и соединить с временной БД до выполнения теста и
    разъединить после выполнения теста"""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # здесь происходит тестирование
    # Teardown : stop db
    tasks.stop_tasks_db()


def test_add_1():
    """tasks.get() использует id, возвращаемый функцией add() при добавлении экземпляра ."""
    # создаем экземпляр именованного кортежа Task
    task = Task('breathe', 'BRIAN', True)
    # закидываем экземпляр в БД,
    # add() при добавлении возвращает task_id
    task_id = tasks.add(task)
    # получить из БД объект, по ранее полученному task_id
    t_from_db = tasks.get(task_id)
    # сравнить оба значения
    # всё, кроме идентификатора должно быть одинаковым
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Проверяем эквивалентность двух задач(объектов taks)"""
    # сравнить все, кроме поля id
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('wake', 'brian'),
                                  Task('breathe', 'Brian', True),
                                  Task('exersice', 'Brian', False)])
def test_add_2(task):
    """ Демонстрирует параметризацию с одним параметром 'task'   """
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    """Демонстрирует параметризацию с несколькими параметрами 'summary', 'owner', 'done'."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# поместим список задач в переменную вне функции
tasks_to_try = (Task('sleep', done=True),
                    Task('wake', 'brian'),
                    Task('wake', 'brian'),
                    Task('breathe', 'BRIAN', True),
                    Task('exercise', 'BrIaN', False))

@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """ Немного разные. """
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# генерация идентификаторов - списковое включение
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Демонстрация параметризации тестовых классов."""

    def test_equivalent(self, task):
        """тест внутри класса."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """можно использовать одни и те же данные или несколько тестов."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id




