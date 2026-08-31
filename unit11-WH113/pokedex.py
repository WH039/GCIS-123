import csv
import random
import pokemon

class Pokedex:
    __slots__ = ['__pokemon_list']

    def __init__(self):
        self.__pokemon_list = []

    def load(self, filename):
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            for record in reader:
                poke = pokemon.Pokemon(record[0], record[1], record[2], record[3])
                self.__pokemon_list.append(pokemon)

    def create_parties(self):
        shuffled_pokemon_list = random.shuffle(self.__pokemon_list)
        index = 0
        party1 = []
        party2 = []
        while index < len(shuffled_pokemon_list):
            party1.append(shuffled_pokemon_list[index])
            party2.append(shuffled_pokemon_list[index+1])
            index += 2
            if index + 1 == 12:
                break
        return party1, party2
    