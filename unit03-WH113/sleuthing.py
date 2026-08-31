"""
A program that demonstrates errors that require looking more deeply into the
code to determine the root cause of the problem.

@author GCCIS Faculty
"""
import math

'''Euler's Number'''
E = 2.718281828459045

def natural_log(x):
    """
    Computes the natural log of x and prints it out before returning it.
    """
    logN = math.log(x, E)
    print("logN(", x, ") = ", logN, sep="")
    return logN

def get_base(side, height):
    """
    Computes and returns the base of an isosceles triangle given the length of 
    one side and the height.
    """
    c_squared = math.pow(side, 2)
    b_squared = math.pow(height, 2)
    return math.sqrt(c_squared - b_squared) * 2

def main():
    """
    Tests the various functions in the class.
    """
    # print a few natural logs
    natural_log(E)
    natural_log(2)
    natural_log(1)
    #natural_log(0)

    # test the isosceles base function
    height = float(input("Enter the height: "))
    side = float(input("Enter the side length: "))
    print("right triangle height:", get_base(height, side))

main()