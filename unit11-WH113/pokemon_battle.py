from pokedex import Pokedex
from pokemon import Pokemon

def battle(party1, party2):
    round = 1
    while len(party1) > 0 or len(party2) > 0:
        #prints round info
        print("Round:", round)
        print("Party 1: {", end=' ')
        for pokem in party1:
            print(Pokemon.repr(pokem)) #prints the repr of every pokemon
        print("}")
        print("Party 2: {", end=' ')
        for pokem in party2:
            print(Pokemon.repr(pokem)) #prints the repr of every pokemon
        print("}")

        #grabs pokemon at first slot
        pokemon1 = party1[0]
        party1.pop(0)
        pokemon2 = party2[0]
        party2.pop(0)
        
        #check types
        if pokemon1.type_compare(pokemon2) == 0:
            print(Pokemon.str(pokemon1), "and", Pokemon.str(pokemon2), "battle to a draw")
        elif pokemon1.type_compare(pokemon2) == 1:
            print(Pokemon.str(pokemon1), "has won the round over", Pokemon.str(pokemon2))
            party1.insert(pokemon1, 0) #returns pokemon to list
            pokemon2.lose_round(pokemon1.get_damage()) #removes health of loser based on dmg of winner
            if pokemon2.is_fainted == True:
                print(Pokemon.str(pokemon2), "has fainted and is out of the battle")
            else:
               party2.insert(pokemon2, 0) 
        elif pokemon1.type_compare(pokemon2) == 2:
            print(Pokemon.str(pokemon2), "has won the round over", Pokemon.str(pokemon1))
            party2.insert(pokemon2, 0) #returns pokemon to list
            pokemon1.lose_round(pokemon2.get_damage()) #removes health of loser based on dmg of winner
            if pokemon1.is_fainted == True:
                print(Pokemon.str(pokemon1), "has fainted and is out of the battle")
            else:
               party1.insert(pokemon1, 0)
        
        #user input used for pause
        input("Press enter for next round")
        round += 1

    #displays winner based on which party still has pokemon
    if len(party1) == 0:
        print("Winning Party:", end = '')
        for poke in party2:
            print(Pokemon.repr(poke), end = '')
    elif len(party2) == 0:
        print("Winning Party:", end = '')
        for poke in party1:
            print(Pokemon.repr(poke), end = '')

def main():
    a_pokedex = Pokedex()
    a_pokedex.load("data/pokemon.csv")
    party1, party2 = a_pokedex.create_parties()
    battle(party1, party2)

main()