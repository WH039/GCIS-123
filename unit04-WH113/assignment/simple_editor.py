# Assignment 4.2
# simple_editor.py by Weicheng Huang

import mystr

# constants
INPUT = 'i'
VIEW = 'v'
REPLACE = 'r'
REPLACE_ALL = 'ra'
QUIT = 'q'

# functions
def handle_view(text_file):
    index = 0
    line = 1
    print(line, ": ", sep = "", end = "")
    line += 1
    while index < len(text_file):
        if text_file[index] == "\n":
            print("\n", line, ": ", sep="", end="")
            line += 1
            index += 1
        else:
            print(text_file[index], end="")
            index += 1

def handle_insert_lines(text_file):
    modified_text = text_file
    insert = input("")
    while True:
        if len(insert) == 1 and ord(insert) == 1:
            break
        else:
            modified_text = modified_text + insert + "\n"
        insert = input()

    return modified_text

def handle_replace(text_file):
    modified_text = text_file
    search_string = input("Search: ")
    replace_string = input("Replace: ")
    modified_text = mystr.replace(modified_text, search_string, replace_string)

    return modified_text

def handle_replace_all(text_file):
    modified_text = text_file
    search_string = input("Search: ")
    replace_string = input("Replace: ")
    modified_text = mystr.replace_all(text_file, search_string, replace_string)

    return modified_text

# main
def main():
    text_file = ""
    while True:
        cmd = input("> ")
        if cmd == QUIT:
            break
        elif cmd == INPUT:
            text_file = handle_insert_lines(text_file)
        elif cmd == VIEW:
            handle_view(text_file)
        elif cmd == REPLACE:
            text_file = handle_replace(text_file)
        elif cmd == REPLACE_ALL:
            text_file = handle_replace_all(text_file)
        else:
            print("Invalid command:", cmd)

main()