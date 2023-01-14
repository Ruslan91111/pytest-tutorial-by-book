"""Демострация tmpdir_factory для создания временных каталогов для области модуля"""

import json
import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Пишем некоторых авторов в файл данных."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    # Фикстура author_file_json() создает временный каталог с именем data и
    # создает файл с именем author_file.json в каталоге данных.
    file = tmpdir_factory.mktemp('data').join('author_file.json')

    print('file:{}'.format(str(file)))

    # Записывает словарь python_author_data как json.
    # Поскольку это фикстура области модуля, json-файл будет создан только один раз
    # для каждого модуля, использующего тест
    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file



