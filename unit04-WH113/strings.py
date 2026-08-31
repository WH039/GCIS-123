# ica 4.11
# strings.py by Weicheng Huang

#functions
def indexing():
    string = "what in the"
    print(len(string))
    print(string[0])
    print(string[len(string)-1])
    print(string[2])
    print(string[6])
    print(string[-1])
    print(string[-11])

def concat():
    a = "cat"
    b = "tail"
    a = a + b

    print(a) #cattail

    x = "age: " + str(18)
    print(x) # age 18

#main
def main():
    indexing()
    concat()

main()