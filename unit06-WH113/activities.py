import arrays
import array_utils
import random
import time
import searches

def making_arrays():
    array1 = arrays.Array(5)
    print(array1)
    array2 = arrays.Array(1, 0)
    print(array2)
    array3 = arrays.Array(10, "")
    print(array3)
    array4 = arrays.Array(20, False)
    print(array4)

def while_fill(an_array):
    index = 0
    while index < len(an_array):
        an_array[index] = index
        index += 1

def for_fill(an_array):
    length = len(an_array)
    
    for index in range(length):
        an_array[index] = index

def roll_the_die(an_array):
    length = len(an_array)

    for index in range(length):
        an_array[index] = random.randint(1, 6)

def linear_search_timer(an_array, target):
    start = time.perf_counter()
    searches.linear_search(an_array, target)
    end = time.perf_counter()
    return end - start

def linear_timer():
    an_array = array_utils.range_array(1, 100000)
    print(linear_search_timer(an_array, 1), "seconds")
    print(linear_search_timer(an_array, 100), "seconds")
    print(linear_search_timer(an_array, 10000), "seconds")

def search_timer(an_array, target, search):
    start = time.perf_counter()
    searches.search(an_array, target)
    end = time.perf_counter()
    return end - start

def timer(search = searches.linear_search):
    an_array = array_utils.range_array(1, 100000)
    print(search_timer(an_array, 1, search), "seconds")
    print(search_timer(an_array, 100, search), "seconds")
    print(search_timer(an_array, 10000, search), "seconds")

def binary_search_timer(an_array, target):
    start = time.perf_counter()
    searches.binary_search(an_array, target)
    end = time.perf_counter()
    return end - start

def print_odds(an_array):
    length = len(an_array)

    for index in range(length):
        if an_array[index] % 2 > 0:
            print(an_array[index], end=" ")
        else:
            continue

def print_odds_rec(an_array, index=0):
    if index >= len(an_array):
        print()
        return
    
    if an_array[index] % 2 > 0:
        print(an_array[index], end=" ")
    
    print_odds_rec(an_array, index + 1)

def countdown(n):
    if n < 0:
        raise ValueError("Undefined")
    
    if n == 0:
        print(n)
        return 0
    
    print(n)
    return n + countdown(n-1)

def factorial(n):
    if n < 0:
        raise ValueError("Undefined")
    
    if n == 0:
        print(n)
        return 0
    
    if n == 1:
        print(n)
        return 1
    
    print(n)
    return n * factorial(n-1)

def count_up(n, count = 0):
    if n < 0:
        raise ValueError("Undefined")
    
    if count == n:
        print(n)
        return n
    
    print(count)
    return count_up(n, count + 1)

def main():
    random.seed(1)
    
    # array_100 = arrays.Array(100,0)
    # index = 0
    # while index < len(array_100):
    #     array_100[index] = index + 1
    #     index += 1
    
    #print(array_100)

    #print_odds(array_100)

    #print_odds_rec(array_100)

    
    making_arrays()
    '''
    array_while = arrays.Array(10, 0)
    print(array_while)
    while_fill(array_while)
    print(array_while)

    array_for = arrays.Array(10, 0)
    print(array_for)
    while_fill(array_for)
    print(array_for)
    

    array_die = arrays.Array(10)
    roll_the_die(array_die)
    print(array_die)
    '''
    #print("sum:",countdown(10))

    #print(factorial(10))

    #print(count_up(10))


main()