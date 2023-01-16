"""Демонстрация работы фикстуры capsys"""
import sys


# Фикстура capsys builtin обеспечивает две функциональные возможности:
# 1) позволяет получить stdout и stderr из некоторого кода,
# 2) временно отключить захват вывода.


def greeting(name):
    print('Hi, {}'.format(name))


# проверить stdout с помощью capsys
def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    assert out == 'Hi, Earthling\n'
    assert err ==''

    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''

# Захваченные stdout и stderr извлекаются из capsys.redouterr().
# Возвращаемое значение — это то, что было зафиксировано с начала функции,
# или с момента последнего вызова.



# проверить stderr с помощью capsys
def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of coffee!' in err


# Использовать capsys.disabled(), чтобы временно пропустить вывод через механизм захвата.
def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nвсегда печатать это')
    print('обычная печать, обычно захваченная')



