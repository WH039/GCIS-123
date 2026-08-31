# Assignment 3.1 by Weicheng Huang

import math

# functions
def fact(n):
    n = int(n)
    if n > 0:
        answer = math.factorial(n)
    if n <= 0:
        answer = 0

    return answer

def root(n):
    if n >= 0.0:
        answer = math.sqrt(n)
    if n < 0.0:
        answer = 0.0

    return answer

def trunk(n):
    answer = math.trunc(n)

    return answer

# main
def main():
    num = input("Please Enter a Number: ")
    num = float(num)
    factorial = fact(num)
    print(factorial)
    square_root = root(num)
    print(square_root)
    truncate = trunk(num)
    print(truncate)

if __name__ == "__main__":
    main()