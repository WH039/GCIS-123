import activities
import random

def test_squared_8():
    #setup
    x = 8
    expected = 64

    #invoke
    actual = activities.squared(x)

    #analyze
    assert actual == expected
    
def test_even_or_odd1():
    #setup
    n = 10
    expected = "even"

    #invoke
    actual = activities.even_or_odd(n)

    #analyze
    assert actual == expected

def test_even_or_odd1():
    #setup
    n = 99
    expected = "odd"

    #invoke
    actual = activities.even_or_odd(n)

    #analyze
    assert actual == expected

def test_coin_toss():
    #setup
    random.seed(1)
    expected = "heads"

    #invoke
    actual = activities.coin_toss()

    #analyze
    assert actual == expected

def test_coin_toss_tails():
    #setup
    random.seed(5)
    expected = "tails"

    #invoke
    actual = activities.coin_toss()

    #analyze
    assert actual == expected
