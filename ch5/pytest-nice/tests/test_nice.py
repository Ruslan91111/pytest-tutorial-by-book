import pytest


def test_pass_fail(testdir):
    # Создать временный тестовый модуль Pytest
    # Фикстура testdir автоматически создает временный каталог для размещения
    # тестовых файлов. Она имеет метод makepyfile(),
    # который позволяет поместить содержимое тестового файла.
    # В нижнем примере мы создаем два теста: один, который проходит и другой, который не проходит.
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 1 == 2  
        """)

    # Запустить pytest для нового тестового файла с помощью testdir.runpytest()
    # Возвращаемое значение имеет тип RunResult.
    result = testdir.runpytest()

    # ret равен 0 для проходящих сеансов и 1 для неудачных сеансов
    # fnmatch_lines выполняет внутренний accept
    result.stdout.fnmatch_lines([
        '*.F*',  # . for Pass, F for Fail
    ])

    # убедитесь, что мы получили код выхода '1' для testsuite
    assert result.ret == 1


# Чтобы не дублировать код, создаем фикстуру, которую можем использовать
# в качестве каталога, уже содержащего наш пример тестового файла.
@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 1 == 2    
            """)
    return testdir


# Используем ранее созданную фикстуру.
def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O*', ])   # . for Pass, O for Fail
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*',
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*'])
    assert result.ret == 1


# Убедимся, что благодарственное сообщение находится в заголовке.
def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running the tests.'])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests.'
    assert thanks_message not in result.stdout.str()


# Проверить текст справки.
# def test_help_message(testdir):
#     result = testdir.runpytest('--help')
#
#     # fnmatch_lines делает внутренний ассерт
#     result.stdout.fnmatch_lines([
#         'nice:',
#         '*--nice*nice: turn FAILED into OPPORTUNITY for improvement',
#     ])
#




