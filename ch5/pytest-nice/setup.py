"""Setup для pytest-nice plugin."""


from setuptools import setup


setup(
    # Здесь только обязательные поля для примера, может быть гораздо больше
    name='pytest-nice',
    version='0.1.0',
    description='Плагин Pytest, чтобы превратить FAILURE в OPPORTUNITY',
    url='https://место/где/содержится/информация/на/этот/пакет',
    author='Минуллин Руслан',    # можно использовать 'maintainer'
    author_email='ruslan_ru911@mail.ru',  # можно использовать 'maintainer_email'
    license='proprietary',
    py_modules=['pytest_nice'],   # Запись py_modules перечисляет pytest_nice.py как наш единственный модуль
                                  # для этого плагина. Хотя это список, и вы можете включить более одного модуля.
    install_requires=['pytest'],
    entry_points={'pytest11': ['nice = pytest_nice', ], }    # До сих пор все параметры setup() стандартные и
    # используются для всех инсталляторов Python. Частью, которая отличается для плагинов Pytest,
    # является параметр entry_points. Функция entry_points является стандартной для setuptools, но pytest11
    # специальный идентификатор, который ищет pytest. В этой строке мы сообщаем pytest, что nice-это имя нашего плагина,
    # а pytest_nice-имя модуля, в котором живет наш плагин.
)



