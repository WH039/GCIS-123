class Pokemon:
    #type hashes
    FIRE = hash('Fire')
    WATER = hash('Water')
    GRASS = hash('Grass')
    
    __slots__ = ['__name', '__type', '__health_points', '__damage_points']

    def __init__(self, name, type, health_points, damage_points):
        self.__name = name
        self.__type = type
        self.__health_points = health_points
        self.__damage_points = damage_points

    #accessor
    def get_damage(self):
        return self.__damage_points
    
    #methods
    def lose_round(self, damage_points):
        self.__health_points -= damage_points
        return self.__health_points
    
    def is_fainted(self):
        if self.__health_points <= 0:
            return True
        else:
            return False
        
    def __str__(self):
        return self.__name
    
    def __repr__(self):
        a_string = self.__name + ":" + self.__type + ":" + str(self.__health_points)
        return a_string
    
    def __hash__(self):
        return hash(self.__type)

    #utilize ints to display type wins
    def type_compare(self, other):
        if hash(self) == hash(other):
            if self.__health_points > other.__health_points:
                return 1
            elif self.__health_points < other.__health_points:
                return 2
            elif self.__health_points == other.__health_points:
                return 0
        if hash(self) == Pokemon.FIRE:
            if hash(other) == Pokemon.WATER:
                return 2
            elif hash(other) == Pokemon.GRASS:
                return 1
        if hash(self) == Pokemon.WATER:
            if hash(other) == Pokemon.GRASS:
                return 2
            elif hash(other) == Pokemon.FIRE:
                return 1
        if hash(self) == Pokemon.GRASS:
            if hash(other) == Pokemon.FIRE:
                return 2
            elif hash(other) == Pokemon.WATER:
                return 1
        
def main():
    p1 = Pokemon("Help", "me", 0, 0)

    print(repr(p1))

main()