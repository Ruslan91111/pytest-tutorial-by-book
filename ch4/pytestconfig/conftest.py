"""Мы будем использовать pytest hook pytest_addoption, чтобы добавить несколько параметров к параметрам,
уже доступным в командной строке pytest:"""

def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")

