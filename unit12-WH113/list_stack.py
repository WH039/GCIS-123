# Assignment 12.1, "list_stack.py"
# by Weicheng Huang

class Stack:
    __slots__ = ['__items']

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0
    
    def push(self, value):
        self.__items.append(value)

    def peek(self):
        return self.__items[0]
        
    def pop(self):
        pop_value = self.__items[0]
        self.__items.pop(0)
        return pop_value
        
    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        string = ''
        for value in self.__items:
            string += str(value) + ', '
        return '[' + string[:-2] + ']'
    
def main():
    stack = Stack()

    stack.push([1,2,3])
    stack.push(2)
    popl = stack.pop()

    print(stack.is_empty())
    for value in popl:
        print(value)

if __name__ == "__main__":
    main()