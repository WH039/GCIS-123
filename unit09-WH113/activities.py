import arrays
import timing
import random
import re

def unique_array (an_array, value):
    for index in range (len (an_array)):
        if value == an_array [index]:
            return
        elif an_array [index] == None:
            an_array [index] = value
            return
        
def fill_array (length):
    an_array = arrays.Array (length)
    for index in range (length):
        unique_array (an_array, index)
    return an_array

def unique_list (a_list, value):
    if value not in a_list:
        a_list.append (value)

def fill_list (length):
    a_list = []
    for index in range (length):
        unique_list (a_list, index)
    return a_list 

def unique_set (a_set, value):
    if value not in a_set:
        a_set.add (value)

def fill_set (length):
    a_set = set ()
    for index in range (length):
        unique_set (a_set, index)
    return a_set

def sets ():
    a_set = {100, 200, 300, 400}
    print (a_set)
    a_set.add (500)
    a_set.add (600)
    print (a_set)
    a_set = set ("lollipop")
    print (a_set)

def coupon_collector (n):
    coupons = set ()
    count = 0
    while len (coupons) < n:
        count += 1
        coupons.add (random.randint (1, n))
    return count

def mixup ():
    a_set = set ("olive")
    for value in a_set:
        print (value, end='')
    print () 

def unique_words(filename):
    word_set = set()
    with open(filename) as file:
        for line in file:
            words = re.findall("\w+'?\w*", line.lower())
            for word in words:
                word_set.add(word)
    return word_set

def intersection(a_set, b_set):
    c_set = set ()
    for value in a_set:
        if value in b_set:
            c_set.add(value)
    
    return c_set

def names():
    a_dict = {}
    a_dict["W"] = "Weicheng"
    a_dict["H"] = "Huang"
    a_dict["J"] = "Jianhua"
    a_dict["H"] = "Huang"

    print(a_dict)

def print_dict(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(key, ":", value)

def main ():
    names()
    print_dict({'h':'e', 'l':'p', 'm':'e'})
    # set1 = {1, 2, 3, 4}
    # set2 = {2, 3, 4, 5}
    # set3 = intersection(set1, set2)
    # print (set3)
    # words = unique_words("data/alice.txt")
    # print (words)
    # print (len(words))
    # mixup ()
    # print (coupon_collector (10000))
    # sets ()
    # an_array = timing.time_function (fill_array, 5000)
    # print (an_array)
    # a_list = timing.time_function (fill_list, 10000)
    # a_set = timing.time_function (fill_set, 5000)

main ()