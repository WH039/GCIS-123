#libraries
import random

#constants
MINIMUM = 1
MAXIMUM = 100

#functions
def secret_number():
    num = random.randrange(MINIMUM, MAXIMUM)
    return num

def check_guess(num, guess):
    guess = int(guess)
    if(num == guess):
        return "correct"
    if(num > guess):
        return "too low"
    if(num < guess):
        return "too high"

#main

def main():
    num = secret_number()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    guess = input("Enter your guess: ")
    result = check_guess(num, guess)
    print(result)
    if(result == "correct"):
        print("You Win!")
        exit()
    print("Out of Guesses")
    print("Correct Number was:", num)
    again = input("Do you want to play again (y/n): ")
    if again == 'y':
        num = secret_number()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        guess = input("Enter your guess: ")
        result = check_guess(num, guess)
        print(result)
        if(result == "correct"):
            print("You Win!")
            exit()
        print("Out of Guesses")
        print("Correct Number was:", num)
    if again == 'n':
        exit()

if __name__ == "__main__":
    main()