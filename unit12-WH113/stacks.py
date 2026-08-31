# Assignment 12.1, "stacks.py"
# by Weicheng Huang

from list_stack import Stack

def process_file(filename):
    main_stack = Stack()
    with open(filename) as file:
        for line in file:
            characters = line.split()
            line_stack = Stack()
            for word in characters:
                line_stack.push(word)
            main_stack.push(line_stack)

    return main_stack

def process_stack(main_stack):
    while main_stack.is_empty() == False:
        line_stack = main_stack.pop()
        string = ''
        while line_stack.is_empty() == False:
            string += line_stack.pop() + ' '
        print (string)

def main():
    walrus = process_file('data\walrus.txt')
    process_stack(walrus)

    strider = process_file('data\strider.txt')
    process_stack(strider)

main()