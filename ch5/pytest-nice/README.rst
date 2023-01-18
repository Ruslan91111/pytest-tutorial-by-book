pytest-nice : A pytest plugin
=============================

Делает вывод pytest немного дружелюбнее во время сбоев.

Особенности
--------
- Включает имя пользователя, выполняющего тесты в выводе pytest.
- Добавляет ``--nice`` опцию, которая:
- превращает ``F`` в ``O``
- с ``-v``, преобразует ``FAILURE`` в ``OPPORTUNITY for improvement``

Установка
------------

Учитывая, что наши плагины Pytest сохраняются в виде .tar.gz в
общей директория PATH, устанавливайте так:

::

$ pip install PATH/pytest-nice-0.1.0.tar.gz
$ pip install --no-index --find-links PATH pytest-nice

Использование
-----

::

$ pytest --nice