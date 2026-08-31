# ascii.py by Weicheng Huang

# global variables
UPPERCASE_A = 'A'
UPPERCASE_G = 'G'
UPPERCASE_Z = 'Z'

# functions
def convert_to_ascii():
    character = input("Please input a character: ")
    code = ord(character)
    print(character, "'s ASCII code is ", code, sep="")

def convert_from_ascii():
    code = input("Please input a code: ")
    code = int(code)
    character = chr(code)
    print(code, "'s character is ", character, sep="")

def alphabet_postition(letter, case):
    code = ord(letter)
    code = code - 64

    print(letter, " is in position ", code, " in the alphabet")

# main
def main():
    #convert_to_ascii()
    #convert_from_ascii()
    alphabet_postition(UPPERCASE_A, UPPERCASE_A)
    #alphabet_postition(global_2)
    #alphabet_postition(global_3)
    
main()