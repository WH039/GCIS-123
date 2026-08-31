import arrays
import practice

"""
Part 1 Tests
"""
# def test_max_empty():
#     #setup
#     array = arrays.Array(0)

#     #invoke
#     actual = practice.max(array)

#     #analyze
#     assert actual == None

# def test_max_len_1():
#     #setup
#     expected = 5
#     array = arrays.Array(1,expected)

#     #invoke
#     actual = practice.max(array)

#     #analyze
#     assert actual == expected

# def test_max_first():
#     #setup
#     expected = 99
#     array = arrays.Array(5)
#     array[0] = expected
#     array[1] = 8
#     array[2] = -1
#     array[3] = 42
#     array[4] = 77

#     #invoke
#     actual = practice.max(array)

#     #analyze
#     assert actual == expected

# def test_max_mid():
#     #setup
#     expected = 99
#     array = arrays.Array(5)
#     array[0] = -1
#     array[1] = 8
#     array[2] = expected
#     array[3] = 42
#     array[4] = 77

#     #invoke
#     actual = practice.max(array)

#     #analyze
#     assert actual == expected

# def test_max_last():
#     #setup
#     expected = 99
#     array = arrays.Array(5)
#     array[0] = -1
#     array[1] = 8
#     array[2] = 77
#     array[3] = 42
#     array[4] = expected

#     #invoke
#     actual = practice.max(array)

#     #analyze
#     assert actual == expected

"""
Part 2 Tests
"""
# def test_power_undefined():
#     #setup
#     base = 999
#     power = -1
#     expected = None

#     #invoke
#     try:
#         actual = practice.power(base,power)
#         assert False,"Exception was expected"

#     #analyze
#     except ValueError:
#         assert True

# def test_power_zero():
#     #setup
#     base = 999
#     power = 0
#     expected = 1

#     #invoke
#     actual = practice.power(base,power)

#     #analyze
#     assert actual == expected

# def test_power_one():
#     #setup
#     base = 42
#     power = 1
#     expected = base

#     #invoke
#     actual = practice.power(base,power)

#     #analyze
#     assert actual == expected

# def test_power_valid():
#     #setup
#     base = 8
#     power = 10
#     expected = 1073741824

#     #invoke
#     actual = practice.power(base,power)

#     #analyze
#     assert actual == expected