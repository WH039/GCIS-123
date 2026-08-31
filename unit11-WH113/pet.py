class Pet:
    CAL_PER_POUND = 3000
    CAL_PER_MILE = 100
    
    __slots__ = ['__species', '__name', '__weight', '__fur_color', '__age']

    def __init__(self, specie, nam, weigh, color):
        self.__species = specie
        self.__name = nam
        self.__weight = weigh
        self.__fur_color = color
        self.__age = 0

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight

    def feed(self, calories):
        pound = calories/Pet.CAL_PER_POUND
        self.__weight += pound

    def walk(self, miles):
        pounds = (miles * Pet.something) / Pet.CAl_PER_POUND
        self.__weight -= pounds


def main():

    pet1 = Pet("Dog", "Wong", 5, 'Brown')

    print(pet1.get_name, pet1.get_weight)
    pet1.feed(10000)
    print(pet1.get_name, pet1.get_weight)
    pet1.walk(2)
    print(pet1.get_name, pet1.get_weight)


main()