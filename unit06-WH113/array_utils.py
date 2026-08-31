import random
import arrays

def random_array(size, min_value=0, max_value=None):
    max_value = size
    
    an_array = arrays.Array(size)

    for index in range(max_value):
        an_array[index] = random.randint(min_value, max_value)

    return an_array

def range_array(start, stop, step=1):
    a_range = range(start, stop, 1)
    an_array = arrays.Array(stop)

    for index in a_range:
        an_array[index] = a_range[index]

    return an_array

def main():
    random.seed(1)
    
    '''array_random = random_array(10)
    print(array_random)'''

    array_range = range_array(0, 10)
    print(array_range)

main()