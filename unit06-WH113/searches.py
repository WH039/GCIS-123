import arrays

def linear_search(an_array, target):
    length = len(an_array)
    num = 0
    found = False

    for index in range(length):
        if an_array[index] == target:
            num = index
            found = True
            break
        else:
            continue

    if found == True:
        return index
    else:
        return None

def binary_search(an_array, target, start = None, end = None):
    if start == None:
        start = 0
        end = len(an_array) - 1
    
    if start > end:
        return None
    
    mid = (start + end) // 2

    if an_array[mid] == target:
        return mid
    elif an_array[mid] < target:
        return binary_search(an_array, target, mid + 1, end)
    elif an_array[mid] > target:
        return binary_search(an_array, target, start, mid - 1)
    
def trinary_search(an_array, target, start = None, end = None):
    if start == None:
        start = 0
        end = len(an_array) - 1
    
    if start > end:
        return None
    
    step = (end - start) // 3
    first_third = start + step
    second_third = end - step

    if an_array[first_third] == target:
        return an_array[first_third]
    elif an_array[second_third] == target:
        return an_array[second_third]
    
    if target < an_array[first_third]:
        return trinary_search(an_array, target, start, first_third - 1)
    elif target < an_array[second_third]:
        return trinary_search(an_array, target, first_third + 1, second_third - 1)
    else:
        return trinary_search(an_array, target, second_third + 1, end)

# def main():
    
#     array_search = arrays.Array(100,0)
#     index = 0
#     while index < len(array_search):
#         array_search[index] = index + 1
#         index += 1
#     print(array_search)       

#     # print(linear_search(array_search, 1))
#     # print(linear_search(array_search, 50))
#     # print(linear_search(array_search, 100))
#     # print(linear_search(array_search, 101))

    
#     # print(binary_search(array_search, 1))
#     # print(binary_search(array_search, 50))
#     # print(binary_search(array_search, 100))
#     # print(binary_search(array_search, 101))

#     # print(trinary_search(array_search, 50))


# main()