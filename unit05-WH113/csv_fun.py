import csv
import re

def names_and_addresses(file):
    with open(file) as a_file:
        next(a_file)
        reader = csv.reader(a_file)
        for record in reader:
            print("Name:", record[0], "address:", record[1])

def first_only(file):
    with open(file) as a_file:
        next(a_file)
        reader = csv.reader(a_file)
        for record in reader:
            print(record[0])

def average(file, col):
    sum_avg = 0.0
    index = 0
    with open(file) as a_file:
        next(a_file)
        reader = csv.reader(a_file)
        for record in reader:
            sum_avg += float(record[col])
            index += 1
        
    avg = sum_avg / index

    print(col, " average: ", avg, sep='')

def zip_check(file):
    with open(file) as a_file:
        next(a_file)
        reader = csv.reader(a_file)
        for record in reader:
            if re.findall("[789]\\d(4)", record[1]):
                print(record[0])

def main():
    #names_and_addresses("data/full_grades_010.csv")
    #first_only("data/full_grades_010.csv")
    #average("data/full_grades_010.csv", 15)
    zip_check("data/full_grades_010.csv")

main()