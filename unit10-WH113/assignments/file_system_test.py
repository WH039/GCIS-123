import file_system

def test_file_1():
    name = 'hello.txt'
    content = 'Hello, World!'
    a_file = file_system.File(name, content)
    assert name == a_file.name
    assert content == a_file.content
    assert False == a_file.is_directory

def test_directory_1():
    name = 'blue_bird'
    a_directory = file_system.Directory(name)
    assert name == a_directory.name
    assert True == a_directory.is_directory



    