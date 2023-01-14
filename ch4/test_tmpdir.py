def test_tmpdir(tmpdir):
    # tmpdir уже имеет имя пути, связанное с ним
    # join() расширяет путь, чтобы включить имя файла,
    # создаваемого при записи в
    a_file = tmpdir.join('something.txt')

    # можно создавать каталог
    a_sub_dir = tmpdir.mkdir('anything')

    # можно создать файлы в директориях (создаются при записи)
    # предыдущее две строчки кода в одном
    another_file = a_sub_dir.join('something_else.txt')

    # эта запись создает 'something.txt'
    a_file.write('contents may settle during shipping')

    # эта запись создает 'anything/something_else.txt'
    another_file.write('something different')

    # также можно прочитать файлы
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'



# Значение, возвращаемое из tmpdir, является объектом типа py.path.local.1,
# но необходимо учитывать, что фикстура tmpdir определена как область действия функции (function scope),
# tmpdir нельзя использовать для создания папок или файлов, которые должны быть доступны дольше, чем одна тестовая ф-я,
# для фикстур с областью видимости, отличной от функции (класс, модуль, сеанс), доступен tmpdir_factory.

def test_tmpdir_factory(tmpdir_factory):
    # Нужно начать с создания каталога, a_dir действует как
    # объект, возвращенный из фикстуры tmpdir
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp будет родительским каталогом 'mydir'
    # нам не нужно использовать getbasetemp(), чтобы
    # показать, что он доступен
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # остальная часть этого теста выглядит так же,
    # как в примере 'test_tmpdir ()', за исключением того,
    # что используется a_dir вместо tmpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'



