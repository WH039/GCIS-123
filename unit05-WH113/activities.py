# activities.py by weicheng huang

import plotter

def numbers():
    file = input("Enter filename:")
    total = 0
    while file != ' ':
        if file == "quit":
            break
            sum = 0
        try:
            with open(file) as a_file:
                for line in a_file:
                    num = line.strip()
                    try:
                        sum += int(num)
                    except ValueError:
                        print("Skipping non-numeric data:", num)
            print("Sum of numbers:", sum)
            total += sum
            
        except FileNotFoundError:
            print("File does not exist:", file)
        #except ValueError:
            #print("File contains non-numeric values")
            
        file = input("Enter filename:")
    print("Total sum:", total)

def division():
    count = 0
    string = input("Enter division: ")
    while string != '':
        value = string.split('/')
        try:
            num = float(value[0])
            den = float(value[1])
            print("=", num/den)
        except ValueError as ve:
            print("Just numbers please")
            count += 1
            if count == 3:
                raise ve
        except ZeroDivisionError as zero:
            print("Did you just try to divided by zero")
            count += 1
            if count == 3:
                raise zero
        stirng = input("Enter division: ")

def password():
    password = input("Enter a password: ")
    if len(password) < 10 or len(password) > 20:
        raise ValueError("Password must be between 10 and 20 character.")
    confirm_password = input("Confirm Password: ")
    if confirm_password != password:
        raise ValueError("Password must match.")
    print("Thank you")



def main():
    #numbers()
    #division()
    #password()


main()