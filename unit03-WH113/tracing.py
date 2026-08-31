"""
A program that demonstrates a few simple errors that are clearly indicated in 
the information provided by the resulting stack trace.

@author GCCIS Faculty
"""
import math

def point_string(x, y):
    """
    Returns the specified point as a string in the format "(x, y)"
    """
    p_string = "(" + str(x) + ", " + str(y) + ")"
    return p_string

def euclidean_distance(x1, y1, x2, y2):
    """
    Computes and returns the Euclidean distance between two points.
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

def main():
    """
    Prints the Euclidean Distance between two points.
    """
    x1 = 0
    y1 = 0
    x2 = 3
    y2 = 4
    print(point_string(x1, y1), "->", point_string(x2, y2), "=",
        euclidean_distance(x1, y1, x2, y2))
    
main()