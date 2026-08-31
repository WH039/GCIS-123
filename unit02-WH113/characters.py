# character.py by Weicheng Huang

# functions
def add_chars(c1, c2):
    # converts the letters to ascii code
    code1 = ord(c1)
    code2 = ord(c2)
    # adds the two code values
    code_total = code1 + code2
    # prints the code total value
    print("The total value of the two characters, ", c1, " and ", c2, " is ", code_total, sep="")

def subtract_chars(c1, c2):
    # converts the letters to ascii code
    code1 = ord(c1)
    code2 = ord(c2)
    # subtracts the two code values
    code_difference = code1 - code2
    # prints the code total value
    print("The value difference of the two characters, ", c1, " and ", c2, " is ", code_difference, sep="")

# main
def main():
    # prompts user to input two letters
    char1 = input("Please enter a character: ")
    char2 = input("Please enter another character: ")
    add_chars(char1, char2)
    subtract_chars(char1, char2)

main()

# no odd character issues

# ord() function can not process anything more than a single character