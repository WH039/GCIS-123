from node import Node

class Stack:
    __slots__ = ['__size', '__top']

    def __init__(self):
        self.__size = 0
        self.__top = None

    def is_empty(self):
        return self.__top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.change_next(self.__top)
        self.__top == new_node
        self.__size += 1

    def peek(self):
        if self.is_empty == True:
            return None
        else:
            return self.__top
        
    def pop(self):
        if self.is_empty == True:
            raise ValueError ("Cannot remove from an empty stack")
        else:
            prev_top = self.__top.get_value()
            self.__top = self.__top.get_next()
            self.__size += 1
            return prev_top
        
    def __len__ (self):
        return 

    def __str__ (self):
        string = ''
        current = self.__top
        while current != None:
            string += str(current.get_value()) + ', '
            current = current.get_next()
        return '[' + string[:-2] + ']'

def main():
    stack = Stack()
    print(stack.is_empty())
    stack.push(0)


main()