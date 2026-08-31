import random

def increasing_comparator(a,b):
    return a < b

def decreasing_comparator(a, b):
    return a > b

def random_list(length):
    list1 = [random.randint(0, length) for _ in range(0,length)]

    return list1

def swap(a_list, a, b):
    temp_var = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = temp_var

    return a_list

def shift(a_list, index, comparator=increasing_comparator):
    while index > 1:
        if comparator(a_list[index], a_list[index - 1]):
            swap(a_list, index, index - 1)
        else:
            break
        index -= 1

def insertion_sort(a_list, comparator=increasing_comparator):
    for index in range(len(a_list)):
        shift(a_list, index, comparator)

def shift_wo_swap(a_list, index, comparator=increasing_comparator):
    target = a_list[index]
    while index > 0:
        if comparator(a_list[index], a_list[index-1]):
            a_list[index] = a_list[index -1]
        else:
            break
        index -= 1
    a_list[index] = target

def insertion_sort_wo_swap(a_list, comparator=increasing_comparator):
    for index in range(len(a_list)):
        shift_wo_swap(a_list, index, comparator)

def split(a_list):
    mid = (len(a_list) + 1) // 2
    return a_list[:mid], a_list [mid:]

def merge (left, right):
    merged = []
    r_index = 0
    l_index = 0
    while l_index < len (left) and r_index < len (right):
        if left [l_index] < right [r_index]:
            merged.append (left [l_index])
            l_index += 1
        else:
            merged.append (right [r_index])
            r_index += 1

    if l_index < len (left):
        merged += left [l_index:]
    else:
        merged += right [r_index:]
    return merged

def merge_sort (a_list):
    if len (a_list) < 2:
        return a_list
    else:
        left, right = split (a_list)
        l_sorted = merge_sort (left)
        r_sorted = merge_sort (right)
        merged = merge (l_sorted, r_sorted)
        return merged 

def bubble_sort(a_list, comparator=increasing_comparator):
    for index in range(len(a_list)):
        try:
            i = a_list[index]
            j = a_list[index + 1]
            if index == len(a_list) - 1:
                break
            elif comparator(i, j):
                swap(a_list, index, index + 1)
                break
            else: 
                continue
        except IndexError:
            return

def partition(a_list, pivot):
    less_than = []
    same_as = []
    more_than = []

    index = 0
    for value in a_list:
        if value > pivot:
            less_than.append(a_list[index])
        elif value < pivot:
            more_than.append(a_list[index])
        elif value == pivot:
            same_as.append(a_list[index])

    return less_than, same_as, more_than

def quicksort(a_list):
    if len(a_list) < 2:
        return list
    else:
        pivot = a_list[0]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)

        return sorted_less, same, sorted_more
    
def quicksort_mid(a_list):
    if len(a_list) < 2:
        return list
    else:
        pivot = a_list[len(a_list)/2]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)

        return sorted_less, same, sorted_more
    
def quicksort_random(a_list):
    if len(a_list) < 2:
        return list
    else:
        pivot = a_list[random.randint(0,len(a_list))]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)

        return sorted_less, same, sorted_more
    
def quick_insertion_sort(a_list, count = 0):
    if len(a_list) < 2:
        return list
    if count > 500:
        return insertion_sort(sorted_less + same + sorted_more)
    else:
        pivot = a_list[random.randint(0,len(a_list))]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)
        
        return sorted_less, same, sorted_more

def main():
    r_list = random_list (9)
    print (split (r_list))
    # print (r_list)
    # insertion_sort_wo_swap (r_list)
    # print (r_list)
    # a_list = list (range (10, 0, -1))
    # print (a_list)
    # shift_wo_swap (a_list, 9)
    # print (a_list)
    # shift_wo_swap (a_list, 9)
    # print (a_list)
    # shift_wo_swap (a_list, 1)
    # print (a_list)
    # shift_wo_swap (a_list, 9)
    # print (a_list)
    

if __name__ == "__main__":
    main()