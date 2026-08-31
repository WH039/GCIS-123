# files.py by Weicheng Huang

import plotter

alice = open("data/alice.txt")
words = open("data/words.txt")
grades = open("data/grades_010.csv")

#function
def print_lines(file):
    for line in file:
        print(line.strip())

def word_search(file):
    search = input("Enter a Word: ")
    found = False
    for line in file:
        if line != search:
            continue
        elif line == search.lower():
            print("Found the Word:", line)
            found = True
            break

    if found == False:
        print("Didn't find the word")
        
def longest_word(string):
    tokens = string.split()
    previous = 0
    longest_w = ""
    for token in tokens:
        longest = len(token)
        if longest > previous:
            previous = longest
            longest_w = token
        else: 
            continue
    if longest_w != '':
        print("Longest word: ", longest_w)

def longest_words(file):
    for line in file:
        longest_word(line.strip())

def print_names(file):
    next(file)
    for line in file:
        split_line = line.split(",")
        print(split_line[1], split_line[0])

def class_average(file,col):
    next(file)
    index = 0
    total = 0
    for line in file:
        split_line = line.split(",")
        total += float(split_line[col])
        index += 1
    average = total / index
    print("Class Average: ", average)

def plot_grades(file, column):
    plotter.init ("Grade Item", "Grade", "Student")
    next(file)
    plotter.new_series("Grades")
    for line in file:
        values = line.strip().split(',')
        plotter.add_data_point(float(values[column]))
    plotter.plot

#main
def main():
    #print_lines(alice)
    #word_search(words)
    #longest_word("ham and spam")
    #longest_words(alice)
    #print_names(grades)
    #class_average(grades,17)
    plot_grades(grades, 3)

    alice.close()
    words.close()
    grades.close()

main()