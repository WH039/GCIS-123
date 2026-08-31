# loops.py by Weicheng Huang

#functions
def count_down(number):
    times = number
    while times >= 0:
        print(times)
        times = times - 1

def count_up(number):
    times = 0
    while times <= number:
        print(times)
        times = times + 1

def sum_of_odds():
    odd_sum = 0
    while True:
        num = int(input("Please enter a number: "))
        if num == 0:
            break
        elif num % 2 == 0:
            continue
        else:
            odd_sum = odd_sum + num

    return odd_sum

def print_range(a_range):
    index = 0
    while index < len(a_range):
        print (a_range [index], end = ' ')
        index += 1
    print ()
    

#main()
def main():
    '''count_down(5)
    count_up(5)
    num = sum_of_odds()
    print(num)'''
    print_range(range(10))
    print_range(range(0,21,2))
    print_range(range(0,21,2))
    print_range(range(10, -1, 1))

main()