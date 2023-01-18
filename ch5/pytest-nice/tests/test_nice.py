import pytest


def test_pass_fail(testdir):
    # Создать временный тестовый модуль Pytest
    # Фикстура testdir автоматически создает временный каталог для размещения
    # тестовых файлов. Она имеет метод makepyfile(),
    # который позволяет поместить содержимое тестового файла.
    # В этом случае мы создаем два теста: один, который проходит и другой, который не проходит.
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 1 == 2  
        """)

    # Запустить pytest для нового тестового файла с помощью testdir.runpytest()
    # Возвращаемое значение имеет тип RunResult.
    result = testdir.runpytest()

    # fnmatch_lines выполняет внутренний accept
    result.stdout.fnmatch_lines([
        '*.F*',  # . for Pass, F for Fail
    ])

    # убедитесь, что мы получили код выхода '1' для testsuite
    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 1 == 2    
            """)
    return testdir
# Теперь, для остальных тестов, мы можем использовать sample_test в качестве
# каталога, который уже содержит наш пример тестового файла.


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O', ])   # . for Pass, O for Fail
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement',
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpyttest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED'])
    assert result.ret == 1










