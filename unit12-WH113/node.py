class Node:
    __slots__ = ['__value', '__next']

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value
    
    def get_next(self):
        return self.__next
    
    def change_value(self, value):
        self.__value = value
    
    def change_next(self, next):
        self.__next = next
    
    def __str__(self):
        return str(self.__value) + " -> " + str(self.__next)

def main():
    node1 = Node(1)

    print(node1)

main()