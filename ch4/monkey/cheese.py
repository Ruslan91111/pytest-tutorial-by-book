# Код пишет dot-файл конфигурации. Поведение некоторых программ может быть изменено с помощью настроек и значений,
# заданных в dot-файле в домашнем каталоге пользователя.

# Код, который читает и записывает cheese-файл персональных настроек.
import os
import json


def read_cheese_preferences():
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


# Функция, не принимает никаких параметров и ничего не возвращает,
# но имеет побочный эффект, записывает файл в домашний каталог текущего пользователя.
def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)


_default_prefs = {
    'slicing': ['manchego', 'sharp cheddar'],
    'spreadable': ['Saint Andre', 'camembert',
                   'bucheron', 'goat', 'humbolt fog', 'camboxola'],
    'salads': ['crumbled feta']
}


