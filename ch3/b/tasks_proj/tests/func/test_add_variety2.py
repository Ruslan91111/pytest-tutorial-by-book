"""
Test the tasks.add() API function. Но теперь, вместо параметризации теста,
мы параметризуем фикстуру под названием a_task.
"""
import pytest
import tasks
from tasks import Task


# кортеж объектов - экземпляров задач
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))


# списковое включение: генерирует данные путем перебора кортежа с объектами-задачами
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]



def equivalent(t1, t2):
    """Проверка  двух задач на равенство."""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


# Теперь, вместо параметризации теста, мы параметризуем фикстуру под названием a_task
# Поле param заполняется одним элементом из списка, назначенного в params
@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """ a_task простая фикстура — она просто возвращает request.param
    в качестве значения для теста, используя его.
    Без идентификатора"""
    return request.param


# Использование фикстуры a_task (без ids).
def test_add_a(tasks_db, a_task):
    """Использование фикстуры a_task (без ids)."""
    # task_id присваивается значение, возвращаемое методом add, при добавлении
    # Task в БД, а добавляется от из кортежа задач
    task_id = tasks.add(a_task)
    # получить из БД задачу по ранее предоставленному task_id
    t_from_db = tasks.get(task_id)
    # сравнить при помощи прописанной ранее функции оба экзепляра - объекта
    assert equivalent(t_from_db, a_task)


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Использование списка идентификаторов."""
    return request.param


def test_add_b(tasks_db, b_task):
    """Использование фикстуры b_task, с идентификаторами."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


# Мы также можем установить параметр ids в функцию, которую мы пишем,
# которая предоставляет идентификаторы. Вот как это выглядит,
# когда мы используем функцию для генерации идентификаторов:

def id_func(fixture_value):
    """Функция для генерации идентификаторов."""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Использование функции (id_func) для генерации идентификаторов."""
    return request.param


def test_add_c(tasks_db, c_task):
    """Использование фикстуры с сгенерированными идентификаторами."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)


# Функция будет вызвана из значения каждого элемента из параметризации.
# Поскольку параметризация представляет собой список объектов Task, id_func() будет вызываться
# с объектом Task, что позволяет нам использовать методы доступа namedtuple для доступа к одному объекту Task
# для генерации идентификатора одного объекта Task за раз.
# Это немного чище, чем генерировать полный список раньше времени, и выглядит одинаково.
# С параметризованными функциями вы можете запускать эту функцию несколько раз.
# Но с параметризованными фикстурами каждая тестовая функция, использующая эту фикстуру, будет вызываться несколько раз


