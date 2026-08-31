'''testing different variable types'''
def variable_practice():
    age_in_month = 300
    num_days_in_year = 365
    pet_name = "Wong"
    pi = 3.1415

    print(age_in_month, num_days_in_year, pet_name, pi, sep="  " )

'''utilizing logical expressions'''
def expressions_practice():
    literal = 1
    addition = 2+2
    exponent = 8**3
    division = 4/2
    mod = 100%3
    pemdas = ((3 + 1) - 2) * 100
    mix = (((100 - 2) * 4) % 20) + 1

    print(literal, addition, exponent, division, mod, pemdas, mix, sep=", ")

'''prompts user to input two numbers to then add, subtract, multiply and divide'''
def promt_and_print():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    print("Add:",num1 + num2)
    print("Subtract:",num1 - num2)
    print("Multiply:",num1 * num2)
    print("Divide:",num1 / num2)

def main():
    variable_practice()
    expressions_practice()
    promt_and_print()

main()