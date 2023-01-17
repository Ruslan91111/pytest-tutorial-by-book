import warnings
import pytest

# Встроенная фикстура recwarn используется для проверки предупреждений,
# генерируемых тестируемым кодом



# Мы хотим прекратить поддерживать функцию, которую нам хотелось бы никогда
# не добавлять в пакет, но пришлось включить для других пользователей.
# Мы можем поместить предупреждение в код и оставить его там для пары выпусков.
def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)



def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == "Please stop using this"


def test_lame_function_2():
    with pytest.warns(None) as warning_list:
        lame_function()

    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'

# Элемент recwarn и диспетчер контекста pytest.warns() обеспечивают аналогичную
# функциональность, поэтому решение о том, что использовать, является исключительно
# вопросом вкуса.
