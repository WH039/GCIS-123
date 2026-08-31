'''
import shells

SHELL = shells.Shell(shells.File_System())

def test_shell():
    assert "/" == SHELL.curr_dir.name
    assert 'Documents' in SHELL.curr_dir.items
    assert 'Downloads' in SHELL.curr_dir.items
    assert [SHELL.curr_dir] == SHELL.curr_dir_path

def test_mkfile():
    shells.mkfile(SHELL, "hello.txt", "Hello!")
    assert 'hello.txt' in SHELL.curr_dir.items
    a_file = SHELL.curr_dir.items["hello.txt"]
    assert "Hello!" == a_file.content


#####  Write a test for mkdir and cd
def test_mkdir():
    assert False  

def test_cd():
    assert False 

'''
