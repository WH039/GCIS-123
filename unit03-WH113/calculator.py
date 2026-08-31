# Assignment 3.2 
# calculator.py by Weicheng Huang

# functions
def add(x, y):
    answer = x + y
    x = str(x)
    y = str(y)
    answer = str(answer)
    string = x + " + " + y + " = " + answer
    return string

def subtract(x, y):
    answer = x - y
    x = str(x)
    y = str(y)
    answer = str(answer)
    string = x + " - " + y + " = " + answer
    return string

def multiply(x, y):
    answer = x * y
    x = str(x)
    y = str(y)
    answer = str(answer)
    string = x + " * " + y + " = " + answer
    return string

def divide(x, y):
    if y == 0:
        x = str(x)
        y = str(y)
        string = x + " / " + y + " = NaN"
        return string
    else:
        answer = x / y
        x = str(x)
        y = str(y)
        answer = str(answer)
        string = x + " / " + y + " = " + answer
        return string

def exponent(x, y):
    answer = x ** y
    x = str(x)
    y = str(y)
    answer = str(answer)
    string = x + " ^ " + y + " = " + answer
    return string

# main
def main():
    x = int(input("Please Enter X: "))
    y = int(input("Please Enter Y: "))
    add_ans = add(x, y)
    print(add_ans)
    sub_ans = subtract(x, y)
    print(sub_ans)
    mul_ans = multiply(x, y)
    print(mul_ans)
    div_ans = divide(x, y)
    print(div_ans)
    exp_ans = exponent(x, y)
    print(exp_ans)

if __name__ == "__main__":
    main()