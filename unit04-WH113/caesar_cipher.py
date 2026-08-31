# caesar_cipher.py by Weicheng Huang

# functions
def encrypt_letter(letter, shift_value):
    if is_alphabetic(letter) == True:
        # translate the letter into ASCII value
        ascii_value = ord(letter)
        # add letter ascii_value with variable shift_value
        ascii_value = ascii_value + shift_value
        # convert the new ascii_value to character
        char = chr(ascii_value)
        #return value
        return char
    else:
        return ' '
    
def decrypt_letter(letter, shift_value):
    # translate the letter into ASCII value
    ascii_value = ord(letter)
    # add letter ascii_value with variable shift_value
    ascii_value = ascii_value - shift_value
    # convert the new ascii_value to character
    char = chr(ascii_value)
    #return value
    return char

def is_alphabetic(char):
    # convert character into ascii value
    ascii_value = ord(char)
    # check if the ascii value is within the alphabet range
    if (ascii_value >= 65 and ascii_value <= 90):
        return True
    else: 
        return False

def encrypt_message(message, shift = 3):
    count = 0
    ciphertext = ""
    while count < len(message):
        ascii_value = ord(message[count])
        ascii_value = ascii_value + shift
        char = chr(ascii_value)
        ciphertext = ciphertext + char
        count = count + 1
    return ciphertext

def decrypt_message(message, shift):
    count = 0
    ciphertext = ""
    while count < len(message):
        ascii_value = ord(message[count])
        ascii_value = ascii_value - shift
        char = chr(ascii_value)
        ciphertext = ciphertext + char
        count = count + 1
    return ciphertext

#main
def main():
    '''letter = input("Please Enter a Letter: ")
    shifted_char = encrypt_letter(letter, 3)
    print(shifted_char)
    letter = input("Please Enter a Letter: ")
    shifted_char = encrypt_letter(letter, 3)
    print(shifted_char)
    letter = input("Please Enter a Letter: ")
    shifted_char = encrypt_letter(letter, 3)
    print(shifted_char)'''
    word = "HELLO"
    m = encrypt_message(word)
    print(m)
    word2 = "KHOOR"
    m2 = decrypt_message(word2, 3)
    print(m2)

if __name__ == "__main__":
    main()