# Assignment 13.1
# Weicheng Huang

import arrays

def give_divisible(num, a_list=[]):
    if num < 3:
        return
    elif num == 3:
        a_list.append(3)
        return a_list
    elif num > 3:
        if (num % 3 ==0 and num % 5 == 0) or (num % 3 != 0 and num % 5 != 0):
            return (num - 1, a_list) 
        elif num % 3 == 0:
            a_list.insert(0, num)
            return(num - 3, a_list)
        elif num % 5 == 0:
            a_list.insert(0, num)
            return(num - 5, a_list)

def find_words(filename, letter, number):
    letter_array = arrays.Array(number)
    count = 0
    with open(filename) as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                while count < number:
                    if word[0] == letter:
                        if word in letter_array:
                            continue
                        else:
                            if count < number:
                                letter_array[count] = word
                                count += 1
                            else:
                                break
    
    return letter_array

def create_calendar(weekday, days):
    calendar = []
    date = 1

    if weekday == 5 and days == 31:
        total_rows = 6
    else:
        total_rows = 5

    for row in range(total_rows):
        week = []
        for day in range(7):
            if(row == 0 and day < weekday):
                week.append(' ')
            elif(date > days):
                week.append(' ')
            else:
                string_day = str(date)
                if(len(string_day) == 1):
                    string_date = '0' + str(date)
                    week.append(string_date)
                    date += 1
                else:
                    week.append(str(date))
                    date += 1
        calendar.append(week)

    return calendar


def main():
    #print(find_words('data/atotc.txt', 'b', 5))

    print(create_calendar(3, 31))


    

main()
                
                    
