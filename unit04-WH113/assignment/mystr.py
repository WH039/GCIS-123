# Assignment 4.1
# mystr.py by Weicheng Huang

# functions
def slice(word, start = 0, end = None):
    if end == None:
         end = len(word)
    count = start
    new_word = "" #new subtring
    if count >= len(word): # checks if the start is greater than the length of the word
        return " "
    if end > len(word): # checks if the end is greater than the length of the word
        end = len(word) - 1
    while count < end:
        new_word = new_word + word[count] # adds letter from old word to new output
        count = count + 1
    return new_word

def contains(string1, string2):
    check = 0
    count1 = 0
    count2 = 0
    while count2 < len(string2):
        while count1 < len(string1):
            if string2[count2] == string1[count1]:
                check = check + 1
            count1 = count1 + 1
            if check == len(string2) - 1:
                start = count1 - count2 - 1
                return start
                break
        count2 = count2 + 1

    if check != len(string2):
        return None

def replace(str1, str2, str3):
    start = 0
    end = len(str2)

    while end < len(str1):
         if slice(str1, start, end) == str2:
              break
         else: 
              start += 1
              end += 1
    
    first = ""
    index = 0
    while index < start:
         first = first + str1[index]
         index += 1

    second = ""
    if end < len(str1):
        index = end
        while index < len(str1):
             second += str1[index]
             index += 1
    
    new_str = first + str3 + second
    return new_str

def replace_all(str1, str2, str3):
    start = 0
    end = len(str2)

    while end < len(str1):
        if slice(str1, start, end) == str2:
            first = ""
            index = 0
            while index < start:
                first = first + str1[index]
                index += 1

            second = ""
            if end < len(str1):
                index = end
                while index < len(str1):
                    second += str1[index]
                    index += 1
            new_str = first + str3 + second
            str1 = new_str
        else: 
            start += 1
            end += 1
    
        
        
    return new_str

def trim(string):
    index = 0
    while index < len(string) and (string[index] == ' ' or string[index] == '\t' or string[index] == '\n'):
            index = index + 1
    
    i = (len(string)-1)
    while i > index and (string[i] == ' ' or string[i] == '\t' or string[i] == '\n'):
            i = i - 1

    new_string = slice(string, index, i+1)

    return new_string

# main
def main():
    text = "cabaab"
    print(slice(text, 2, 5))
    print(slice(text, 2))
    print(slice(text, end = 5))
    print(contains(text, "ab"))
    print(replace("bluedotbluedot", "dot", "spot"))
    print(replace_all("bluedotsreddotspurpledotshelp", "dot", "-----"))
    print(trim("\t\n aa a \ta\n"))

if __name__ == "__main__":
    main()
    