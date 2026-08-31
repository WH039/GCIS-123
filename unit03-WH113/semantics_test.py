import semantics
import math

def test_rectangle_area_4_5():
    # setup
    height = 4
    width = 5
    expected = 20

    # invoke
    actual = semantics.rectangle_area(height, width)

    # analyze
    assert expected == actual

def test_average():
    # setup
    a = 99
    b = 97
    c = 90
    d = 85
    expected = 92.75

    # invoke
    actual = semantics.average(a, b, c, d)

    # analyze
    assert math.isclose(expected, actual)

def test_five_factorial():
    # setup
    expected = 120

    # invoke
    actual = semantics.five_factorial()

    # analyze
    assert expected == actual

def test_square_root_2():
    # setup
    x = 2
    expected = 1.4142135623730951

    # invoke
    actual = semantics.square_root(2)

    # analyze
    assert math.isclose(expected, actual)
