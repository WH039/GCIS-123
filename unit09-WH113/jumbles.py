# Assignment 9.2 "jumbles.py"
# by Weicheng Huang

# Libraries

# Global Variables

# Functons
def filetolist(filename):
    word_list = []
    with open(filename) as file:
        for line in file:
            word_list.append(line.strip().lower())
    
    return word_list

def sortword(string):
    sorted_string = sorted(string)
    key = ""
    for letter in sorted_string:
        key += letter

    return key

def createdictionary(a_list):
    jumbles = {}
    for index in range(len(a_list)):
        key = sortword(a_list[index])
        if key in jumbles:
            jumbles[key].append(a_list[index])
        else:
            jumbles[key] = [a_list[index]]

    return jumbles

def findwordmatch(string, dictionary):
    key = sortword(string)
    if key in dictionary:
        if len(dictionary[key]) == 1:
            return dictionary[key]
        else:
            word_list = dictionary[key]
            for index in range(len(word_list)):
                print(index, ":", word_list[index])
            choice = int(input("Enter the index of a word: "))
            return word_list[choice]

                
def findclue(dictionary):
    letters = ""
    clue = str(input("Enter clue: "))
    clueclue = clue.split(' ')
    index1 = int(clueclue[1])
    if len(clueclue) > 2:
        index2 = int(clueclue[2])
    word = findwordmatch(clueclue[0], dictionary)
    print(word[0])
    letters += word[0][index1]
    if len(clueclue) > 2:
        letters += word[0][index2]
    
    return letters

# main
def main():
    word_list = filetolist("data/words.txt")
    word_dictionary = createdictionary(word_list)
    # print(word_dictionary)
    unsolved_letters = []
    unsolved_letters.append(findclue(word_dictionary))
    unsolved_letters.append(findclue(word_dictionary))
    unsolved_letters.append(findclue(word_dictionary))
    unsolved_letters.append(findclue(word_dictionary))
    completed_word = sortword(unsolved_letters)
    solution = findwordmatch(completed_word, word_dictionary)
    print("Solution:", solution)

    #findwordmatch("aet", word_dictionary)
    # print(sortword("help"))


main()