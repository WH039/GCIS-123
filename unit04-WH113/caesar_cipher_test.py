import caesar_cipher

def test_encrypt_letter1():
    #setup
    letter = '!'
    expected = ' '

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, 3)

    #analyze
    assert actual == expected

def test_encrypt_letter2():
    #setup
    letter = 'G'
    expected = 'L'

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, 5)

    #analyze
    assert actual == expected

def test_encrypt_letter3():
    #setup
    letter = '2'
    expected = ' '

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, 10)

    #analyze
    assert actual == expected

def test_encrypt_letter4():
    #setup
    letter = 'T'
    expected = 'U'

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, 1)

    #analyze
    assert actual == expected

def test_decrypt_letter1():
    #setup
    letter = 'B'
    expected = 'A'

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, 1)

    #analyze
    assert actual == expected

def test_decrypt_letter2():
    #setup
    letter = 'X'
    expected = 'U'

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, 3)

    #analyze
    assert actual == expected

def test_decrypt_letter3():
    #setup
    letter = 'H'
    expected = 'C'

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, 5)

    #analyze
    assert actual == expected

def test_decrypt_letter4():
    #setup
    letter = 'Z'
    expected = 'P'

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, 10)

    #analyze
    assert actual == expected

def test_is_alphabetic1():
    #setup
    char = 'A'
    expected = True

    #invoke
    actual = caesar_cipher.is_alphabetic(char)

    #analyze
    assert actual == expected

def test_is_alphabetic2():
    #setup
    char = '!'
    expected = False

    #invoke
    actual = caesar_cipher.is_alphabetic(char)

    #analyze
    assert actual == expected

def test_is_alphabetic3():
    #setup
    char = 'R'
    expected = True

    #invoke
    actual = caesar_cipher.is_alphabetic(char)

    #analyze
    assert actual == expected

def test_encrypted_message1():
    #setup
    message = "HELLO"
    expected = "KHOOR"
    #invoke
    actual = caesar_cipher.encrypt_message(message)
    #analyze
    assert expected == actual

def test_encrypted_message2():
    #setup
    message = "WASTE"
    shift = 2
    expected = "YCUVG"
    #invoke
    actual = caesar_cipher.encrypt_message(message, shift)
    #analyze
    assert expected == actual

def test_encrypted_message1():
    #setup
    message = "KHOOR"
    shift = 3
    expected = "HELLO"
    #invoke
    actual = caesar_cipher.decrypt_message(message, shift)
    #analyze
    assert expected == actual

def test_encrypted_message2():
    #setup
    message = "EPOUMPPLCFIJOEZPV"
    shift = 1
    expected = "DONTLOOKBEHINDYOU"
    #invoke
    actual = caesar_cipher.decrypt_message(message, shift)
    #analyze
    assert expected == actual