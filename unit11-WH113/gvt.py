COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ['__name', '__cost', '__rarity', '__faction', '__attack', '__health']

    def __init(self, name, cost, rarity, faction, attack, health):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__faction =  faction
        self.__attack = attack
        self.__health = health

    def __repr__ (self):
        return "[{}{} {:02d} {:02d} {:02d}]".format (self.__name[0], self.__faction[0], self.__cost,
                                                     self.__attack, self.__health)
    
    def __eq__ (self, other):
        if type (self) == type (other):
            return self.__faction == other.__faction and \
                   self.__rarity == other.__rarity and \
                   self.__cost == other.__cost and \
                   self.__attack == other.__attack
        else:
            return False
        
    def __lt__ (self, other):
        if type (self) == type (other):
            if self.__cost == other.__cost:
                return self.__name < other.__name
            else:
                return self.__cost < other.__cost
        else:
            return False

    def get_name (self):
        return self.__name
    
    def get_cost (self):
        return self.__cost
    
    def get_rarity (self):
        return self.__rarity
    
    def get_faction (self):
        return self.__faction
    
    def get_attack (self):
        return self.__attack
    
    def get_health (self):
        return self.__health
    
    def damage (self, amount):
        remainaing = self.__health - amount
        if remainaing < 0:
            self.__health = 0
            return -remainaing
        else:
            self.__health = remainaing
            return 0

    def is_conscious (self):
        return self.__health > 0
    
import goatils
import random
def make_card (faction, rarity):
    if faction == 'GOAT':
        name = goatils.make_goat_name ()
    else:
        name = TROLLS [random.randrange (0, len (TROLLS))]
    if rarity == COMMON:
        points = 8
        cost = (1, 3)
    elif rarity == UNCOMMON:
        points = 12
        cost = (2, 5)
    elif rarity == RARE:
        points = 16
        cost = (4, 7)
    else:
        points = 24
        cost = (10, 10)
    
    health = random.randint (1, points)
    attack = points - health
    cost = random.randint (cost[0], cost [1])

    return Card (name,cost, rarity, faction, attack, health)

def make_deck (faction):
    deck = [make_card (faction, COMMON) for _ in range (20)]
    deck += [make_card (faction, UNCOMMON) for _ in range (10)]
    deck += [make_card (faction, RARE) for _ in range (8)]
    deck += [make_card (faction, LEGENDARY) for _ in range (2)]
    random.shuffle (deck)
    return deck