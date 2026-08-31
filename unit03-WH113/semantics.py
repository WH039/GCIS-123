import math

def rectangle_area(height, width):
    """
    Returns the area of a rectangle with the specified height and width.
    """
    return height * width 

def average(a, b, c, d):
    """
    Returns the average of 4 numbers.
    """
    return (a + b + c + d) / 4

def five_factorial():
    """
    Returns 5!
    """
    return 5 * 4 * 3 * 2 * 1

def square_root(x):
    """
    Returns the square root of x.
    """
    return math.sqrt(x)

def main():
    area = rectangle_area(4, 5)
    print("the area of a 4x5 rectangle:", area)

    print("the average of 99, 97, 90, and 85:", average(99, 97, 90, 85))

    print("5!:", five_factorial())

    print("the square root of 2:", square_root(2))

if __name__ == "__main__":
    main()