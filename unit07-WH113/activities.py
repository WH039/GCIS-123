import arrays
import array_utils
import random

def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for value in a_tuple:
        print(value)

def packer():
    x = 'a'
    y = True
    z = 5
    zz = "help"

    return x, y, z, zz

def lists():
    list1 = ['a', "help", 4, True, 5]
    index = 0
    a_range = range(len(list1))

    for index in a_range:
        print(index, ": ", list1[index], sep="")

    return list1

def make_list(a_sequence):
    a_list = []
    for value in a_sequence:
        a_list.append(value)

    return a_list

def scale(a_list, scalar):
    length = len(a_list)
    index = 0

    while index < length:
        a_list[index] = a_list[index] * scalar
        index += 1

    return a_list
    
def mutater(a_list, an_int):
    print(a_list)
    print(an_int)

    an_int = an_int * 5
    a_list[0] = a_list[0] * 5

    print(a_list)
    print(an_int)

def cat(a_list, b_list):
    c_list = a_list + b_list

    return c_list

def appender(a_list, b_list):
    a_list += b_list

    return a_list

def inserter(a_list, value):
    index = len(a_list) // 2

    a_list.insert(index, value)

    return a_list

def popper(a_list):
    print(a_list)
    while len(a_list) > 0:
        a_list.pop()
        print(a_list)

def array_insert(an_array, index, value):
    array_in = arrays.Array(len(an_array))
    ind = 0
    while ind < len(array_in):
        if ind == index:
            array_in[ind] = value
            ind += 1
        else:
            array_in[ind] = an_array[ind]
            ind += 1

    return array_in

def array_pop(an_array, index):
    array_out = arrays.Array(len(an_array)-1)
    ind = 0
    while ind < len(array_out):
        if ind >= index:
            array_out[ind] = an_array[ind+1]
            ind += 1
        else:
            array_out[ind] = an_array[ind]
            ind += 1

    return array_out

def rgb_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    a_tuple = (r, g, b)

    return a_tuple

def tuple_equality(tuple_a, tuple_b):
    print(tuple_a)
    print(tuple_b)

    compare_is = tuple_a is tuple_b
    print (compare_is)
    compare_eq = tuple_a == tuple_b
    print (compare_eq)

def reverse_sequence(list_in):
    list_out = []
    index = len(list_in) - 1

    while index >= 0:
        list_out.append(list_in[index])
        index -= 1

    return list_out

def slices():
    string = "Try the stuffed crust..."
    
    print(string)
    last_space = 0
    index = 0
    while index < len(string):
        if string[index] == ' ' or string[index] == '.':
            print(string[last_space:index])
            last_space = index + 1
            index += 1
        else:
            index += 1

def dices(a_list):
    if len(a_list) == 0:
        print()
        return
    
    index = random.randrange(len(a_list))
    print(a_list[index], end='')
    a_list = a_list[:index] + a_list[index + 1:]
    dices(a_list)

def swapper(a_list):
    first_half = []
    second_half = []

    for index in range(len(a_list)):
        if index < len(a_list) // 2:
            first_half.append(a_list[index])
        else:
            second_half.append(a_list[index])

    new_list = second_half + first_half
    return new_list

def chunky(a_list, size):
    for index in range(len(a_list)):
        print(a_list[index:index+size])

def comprehension():
    list1 = [char for char in "foobar"]
    print(list1)
    list2 = [0 for _ in range(10)]
    print(list2)
    list3 = [n for n in range(0,13)]
    print(list3)
    list4 = [n for n in range(0,22,2)]
    print(list4)
    list5 = [n//3 for n in range(0, 51)]
    print(list5)

def make_table(rows, columns, value):
    table=[]
    for row in range(rows):
        inner = []
        table.append(inner)
        for col in range(columns):
            inner.append(value)

    # table = [[value for col in range(columns)] for row in range(rows)]

    return table

def random_list (size):
    a_list = []
    for _ in range (size):
        a_list.append (random.randint (0, 100))
    return a_list

def sorted_test (a_list):
    b_list = sorted (a_list, reverse=True)
    print (a_list)
    print (b_list)

def sort_test (a_list):
    print (a_list)
    a_list.sort (reverse=True)
    print (a_list)

def sort_cards (hand):
    print (hand)
    hand.sort (key = suit_key)
    print (hand)

def suit_key (card):
    rank, suit = card
    return suit, rank

def main():
    # a_tuple = (1, "what", False)
    # tuples(a_tuple)

    # a, b, c, d = packer()
    # print(a, b, c, d)

    # print(lists())

    # a_sequence = [1, 2, 3, 4, 5]
    # list2 = ['h', 'e', 'l', 'p']
    # print(make_list(a_sequence))
    # print(scale(make_list(a_sequence), 2))

    # mutater(a_sequence, 3)
    # print(a_sequence)
    # print(list2)
    # print(cat(a_sequence, list2))
    # print(appender(a_sequence, list2))
    # print(inserter(list2, 'g'))
    # popper(list2)

    # array1 = array_utils.range_array(0, 10)
    # print (array1)
    # print(array_insert(array1, 2, 1))
    # print(array_pop(array1, 1))

    # print(rgb_tuple())
    # print(rgb_tuple())
    # print(rgb_tuple())

    # list_a = ["help", 2, False]
    # tuple_a = tuple(list_a)
    # tuple_b = tuple(list_a)
    # tuple_equality(tuple_a, tuple_b)
    # tuple_c = (2, False, "Help")
    # tuple_equality(tuple_a, tuple_c)

    # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(reverse_sequence(list1))

    # list2 = ['h', 'e', 'l', 'p']
    # slice = list2[:1]
    # print(slice)

    # slices()

    # dices()

    # print(swapper(list1))

    # chunky(list1, 2)

    # comprehension()

    print(make_table(4, 4, 0))

main()