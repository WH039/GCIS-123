import arrays

class Queue:
    __slots__ = ['__elements', '__front', '__back', '__length']

    def __init__(self):
        self.__elements = arrays.Array(3)
        self.__front = 0
        self.__back = 0
        self.__length = 0

    def __str__(self):
        string = ""
        for index in range(len(self.__elements)):
            string = string + self.__elements[index] + ", "
        return '['+ string [:-2] + ']'
    
    def __len__(self):
        return self.__length
    
    def is_empty(self):
        return self.front == self.__back
    
    def __increment(self, index):
        index += 1
        if index == len(self.__elements):
            index = 0
        return index
    
    def __resize(self):
        new_elements = arrays.Array(self.__length * 2)
        new_index = 0
        old_index = self.__front
        while old_index != self.__back:
            new_elements[new_index] = self.__elements[old_index]
            new_index += 1
            old_index = self.__increment(old_index)
        self.__front = 0
        self.__back = self.__length
        self.__elements = new_elements
    
    def enqueue(self, value):
        self.__elements[self.__back] = value
        self.__back = self.__increment(self.__back)
        self.__length += 1

    def dequeue(self):
        value = self.__elements[self.__front]
        self.__elements[self.__increment] = None
        self.__front = self.__increment(self.__front)
        self.__length -= 1
        return value