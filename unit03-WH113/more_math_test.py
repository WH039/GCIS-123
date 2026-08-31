import more_math
import math

def test_fact():
    #setup
    n = 4
    expected = 24

    #invoke
    actual = more_math.fact(n)

    #analyze
    assert actual == expected

def test_root():
    #setup
    n = 4
    expected = 2

    #invoke
    actual = more_math.root(n)

    #analyze
    assert math.isclose(actual,expected)

def test_trunk():
    #setup
    n = 4.00
    expected = 4

    #invoke
    actual = more_math.trunk(n)

    #analyze
    assert math.isclose(actual,expected)