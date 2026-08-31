import csv
import arrays

def start_with(filename, letter):
    count = 0
    with open(filename) as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word[0] == letter:
                    count += 1

    return count

def zip_lookup(filename, zip_code):
    with open(filename) as a_file:
        reader = csv.reader(a_file)
        for zip, city in reader:
            if zip == zip_code:
                return city
    raise ValueError(str(zip_code) + " is an invalid zip code")

def is_power(a, b):
    if a == 1:
        return True
    
    elif a % b == 0:
        return is_power(a / b, b)
    
    else:
        return False

def fill_array(an_array, start = 0, step = 1, index = 0):
    if index == len(an_array):
        return 
    else:
        an_array[index] = start + index * step
        return fill_array(an_array, start, step, index, + 1)
    
def tuplify(first, last, middle = ''):
    if middle == '':
        a_tuple = (first, last)
    else:
        a_tuple = (first, middle, last)
    return a_tuple

def cubed(a_list):
    cubed_list = []
    for value in a_list:
        cubed_list.append(value ** 3)
    return cubed_list

def table(rows, column):
    a_table = list(rows)
    for index in range(len(a_table)):
        a_table[index] = list(column)

    return a_table

def main():

    a_table = table(4, 5)
    for row in a_table:
        print(row)
    
    list1 = [1, 2, 3, 4, 5]
    print(cubed(list1))

    print(tuplify())

    an_array = arrays.Array(10)
    fill_array(an_array, 6, 1)
    print(an_array)
    
    print(is_power(81, 9))
    print(is_power(40, 5))

    zip = 'blank'
    while zip != '':
        try:
            zip = input("Enter zip code: ")
            print(zip_lookup("data/zip_codes.csv"))
        except FileNotFoundError:
            print("Cannot open zip file")
            break
        except ValueError as ve:
            if zip != '':
                print(ve)