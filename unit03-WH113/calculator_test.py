# Assignment 3.2
# calculator_test.py by Weicheng Huang

import calculator

#add
def test_add():
    #setup
    x = 5
    y = 7
    expected = "5 + 7 = 12"

    #invoke
    actual = calculator.add(x, y)

    #analyze
    assert actual == expected


#subtract
def test_subtract():
    #setup
    x = 2
    y = 17
    expected = "2 - 17 = -15"

    #invoke
    actual = calculator.subtract(x, y)

    #analyze
    assert actual == expected

#multiply
def test_multiply():
    #setup
    x = 3
    y = 9
    expected = "3 * 9 = 27"

    #invoke
    actual = calculator.multiply(x, y)

    #analyze
    assert actual == expected

#divide
def test_divide():
    #setup
    x = 100
    y = 0
    expected = "100 / 0 = NaN"

    #invoke
    actual = calculator.divide(x, y)

    #analyze
    assert actual == expected

#exponent
def test_exponent():
    #setup
    x = 10
    y = 3
    expected = "10 ^ 3 = 1000"

    #invoke
    actual = calculator.exponent(x, y)

    #analyze
    assert actual == expected