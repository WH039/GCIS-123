#Assignment 10.1

class File:

    __slots__ = ['name', 'content', 'is_directory']

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.is_directory = False

class Directory:

    __slots__ = ['name', 'directories', 'is_file']

    def __init__(self, name):
        self.name = name
        self.content = {}
        self.is_file = False

    def add_content(self, dir):
        if dir.name in self.content:
            print("Directory already exists")
        else:
            self.content[dir.name] = dir

class File_System:

    __slots__ = ['root']

    def __init__(self):
        self.root = Directory("/")
        self.root.add_content(Directory("Documents"))
        self.root.add_content(Directory("Downloads"))

def print_file(a_file):
    print("Name = ", a_file.name, ", Size = ", len(a_file.content), sep = '')
    print(a_file.content)

def print_dir(a_directory):
    print("Name =", a_directory.name)
    items = []
    for name, content in a_directory.content:
        if content.is_file == False:
            items.append(name + "(d)")
        elif content.is_directory == False:
            items.append(name + str(len(content.content)))
    
    return items

def print_file_system(file_sys):
    print_dir(file_sys)

def add_item(dir, item):
    return dir.add_item(item)

def build_file_system():
