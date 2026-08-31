# in class activites

#libraries
import math
import random

#constants
pi = 3.14159

#function
def circle_area(radius):
    return pi * math.pow(radius, 2)

def circle_circumference(radius):
    return pi * radius * 2


def squared(x):
    return math.pow(x, 2)

def cubed(x):
    return math.pow(x, 3)

def hypotenuse(adjacent, opposite):
    a = math.pow(adjacent, 2)
    b = math.pow(opposite, 2)

    return math.sqrt(a+b)

def even_or_odd(n):
    if (n % 2 == 0):
        return "even"
    else:
        return "odd"
    
def coin_toss():
    number = random.randrange(1,3)
    if number == 1:
        return "heads"
    if number == 2:
        return "tails"


#main
def main():
    '''area = circle_area(10)
    print(area)
    num = squared(2)
    print(num)
    num = cubed(2)
    print(num)
    even_odd = even_or_odd(10)
    print(even_odd)
    heads_or_tails = coin_toss()
    print(heads_or_tails)

    random.seed(100)

    x = random.randint(1, 50)
    y = random.randint(1, 50)
    z = random.randint(1, 50)
    print(x, y, z)'''

    area = circle_area(10)
    print(area)
    circumference = circle_circumference(10)
    print(circumference)

main()

'''
3.3
false
true
true
true
false
false
true
false
true
false
'''

'''
3.4
false
true
true
false
false
true
true
false
true
false
true
?
'''

'''
syntax errors, easiest to see what's wrong

yes, only took a few seconds at most

system errors, mostly with git

it took longer to see what was wrong when git would paste a block of text for me to read
'''

'''
Type error

attribute error

value error

attribute error

Type error

value error
'''