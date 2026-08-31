import guessing_game
import random

def test_secret_number():
    #setup
    random.seed(1)
    expected = 18

    #invoke
    actual = guessing_game.secret_number()

    #test
    assert actual == expected
    