# Assignment 12.2

import csv

class Tasks:
    __slots__ = ['__name', '__location']

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def __str__(self):
        string = self.__name + ' in ' + self.__location
        return string
    
def read_file(filename):
    task_list_full = []
    with open(filename) as file:
        next(file)
        line = file.csv.reader(file)
        for item in line:
            task = [item[0], item[1]]
            task_list_full.append(task)
    
    return task_list_full
