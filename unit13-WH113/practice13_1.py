# Assginment 13.1
# Weicheng Huang

import csv

def find_streets(filename, street_name):
    try:
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            for street, street_type, post_direction in reader:
                if street == street_name:
                    print(street, street_type, post_direction, sep='  ')
    except FileNotFoundError:
        print("The file does not exist")

def popular_street(filename):
    try:
        highest_street = ''
        highest_count = 0
        prev_street = ''
        count = 1
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            for street, street_type, post_direction in reader:
                if prev_street == street:
                    count += 1
                else:
                    count = 1
                    prev_street = street
                if highest_count < count:
                    highest_count = count
                    highest_street = street
                elif highest_count >= count:
                    continue
            return highest_street
    except FileNotFoundError:
        print("The file does not exist")
