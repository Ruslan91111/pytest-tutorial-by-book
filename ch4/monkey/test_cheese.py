import copy

import cheese


def test_def_prefs_full():
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


# Создадаем временный каталог и перенаправляе HOME,
# чтобы указать на этот новый временный каталог.
def test_def_prefs_change_home(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


# Для Windows плохо
# Вместо исправления переменной окружения HOME, запатчим expanduser.
def test_def_prefs_change_expanduser(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheese.os.path, 'expanduser',
                        lambda x: x.replace('~', str(fake_home_dir)))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


# Мы хотим быть уверенным, что если файл уже существует, то он
# будет перезаписан по умолчанию, когда вызывается.
def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # Запись в файл один раз
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr((cheese.os.path, 'expanduser',
                         lambda x: x.replace('~', str(fake_home_dir))))
    cheese.write_default_cheese_preferences()
    defaults_before=copy.deepcopy(cheese._default_prefs)

    # изменение значений по умолчанию
    monkeypatch.setitem(cheese._default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['pepper jack'])
    defaults_modified = cheese._default_prefs

    # Перезапись его измененными значениями по умолчанию
    cheese.write_default_cheese_preferences()

    # чтение и провека
    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before


