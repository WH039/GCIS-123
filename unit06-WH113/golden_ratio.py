# Assignment 6.1
# Weicehng Huang

#libraries
import arrays

#constants


#functions
def fibonacci(n):
    if n <= 0:
        raise ValueError("What")
    
    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def fill_fibonacci_array(an_array, index = 0):
    if index < 0:
        raise ValueError("What")
    
    if index == 0:
        an_array[index] = 0

    
    if index == 1 or index == 2:
        an_array[index] = 1

    if index >= len(an_array):
        return
    
    an_array[index] = fibonacci(index+1)
    fill_fibonacci_array(an_array, index + 1)

def print_ratio(an_array, index = 0):
    if index < 0:
        raise ValueError("What")

    if index >= len(an_array):
        return
    try:
        a = an_array[index]
        b = an_array[index + 1]
        print(f"{a:>4n} {b:>4n}  {(b/a):.5f}  {((a+b)/b):.5f}")
        print_ratio(an_array, index + 1)
    except ZeroDivisionError:
        print(f"{a:>4n} {b:>4n}", "undefined")
        print_ratio(an_array, index + 1)
    except IndexError:
        return

#main
def main():
    #print(fibonacci(9))

    array_fill = arrays.Array(20)
    fill_fibonacci_array(array_fill)
    print(array_fill)

    print_ratio(array_fill)

main()