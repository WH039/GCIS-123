from sorts import *

def test_split_even ():
    # Setup
    an_array = [1, 2, 3, 4, 5, 6]

    # invoke
    left, right = split (an_array)

    # analysis
    assert left == [1, 2, 3]
    assert right == [4, 5, 6]

def test_split_odd ():
    # Setup
    an_array = [1, 2, 3, 4, 5]

    # invoke
    left, right = split (an_array)

    # analysis
    assert left == [1, 2, 3]
    assert right == [4, 5]

def test_merge_singles ():
    # Setup
    left = [3]
    right = [2]

    # invoke
    merged = merge (left, right)

    # analysis
    assert merged == [2, 3]

def test_merge_dobules ():
    # Setup
    left = [3, 4]
    right = [2, 5]

    # invoke
    merged = merge (left, right)

    # analysis
    assert merged == [2, 3, 4, 5]

def test_merge_uneven ():
    # Setup
    left = [1, 3, 4]
    right = [2, 5]

    # invoke
    merged = merge (left, right)

    # analysis
    assert merged == [1, 2, 3, 4, 5]

def test_merge_left_first ():
    # Setup
    left = [1, 2, 3]
    right = [4, 5, 6]

    # invoke
    merged = merge (left, right)

    # analysis
    assert merged == [1, 2, 3, 4, 5, 6]

def test_merge_right_first ():
    # Setup
    left = [4, 5, 6]
    right = [1, 2, 3]

    # invoke
    merged = merge (left, right)

    # analysis
    assert merged == [1, 2, 3, 4, 5, 6]

def test_merge_sort_empty ():
    # Setup
    a_list = []

    # invoke
    sorted = merge_sort (a_list)

    # analysis
    assert sorted == []

def test_merge_sort_lone ():
    # Setup
    a_list = [1]

    # invoke
    sorted = merge_sort (a_list)

    # analysis
    assert sorted == [1]

def test_merge_sort_two_unsorted ():
    # Setup
    a_list = [4, 2]

    # invoke
    sorted = merge_sort (a_list)

    # analysis
    assert sorted == [2, 4]

def test_merge_sort_three_unsorted ():
    # Setup
    a_list = [4, 2, 3]

    # invoke
    sorted = merge_sort (a_list)

    # analysis
    assert sorted == [2, 3, 4]

def test_merge_sort_four_sorted ():
    # Setup
    a_list = [1, 3, 4, 7]

    # invoke
    sorted = merge_sort (a_list)

    # analysis
    assert sorted == [1, 3, 4, 7]

def test_partition_one_each():
    #setup
    a_list = [2, 3, 1]
    #invoke
    less, same, more = partition(a_list, 2)
    #analyze
    assert less == [1]
    assert same == [2]
    assert more == [3]

def test_partition_one_each():
    #setup
    a_list = [3, 2, 1]
    #invoke
    less, same, more = partition(a_list, 2)
    #analyze
    assert less == [1]
    assert same == [2]
    assert more == [3]

def test_quicksort_lone():
    #setup
    a_list = [1]
    #invoke
    output = quicksort(a_list)
    #analyze
    assert output == [1]

def test_quicksort1():
    #setup
    a_list = [2 ,5 ,6, 3, 1]
    #invoke
    output = quicksort(a_list)
    #analyze
    assert output == [1, 2, 3, 5, 6]

def test_quicksort2():
    #setup
    a_list = [1, 4, 6, 8, 9]
    #invoke
    output = quicksort(a_list)
    #analyze
    assert output == [1, 4, 6, 8, 9]

def test_quicksort3():
    #setup
    a_list = [10, 7 , 4, 2, 1]
    #invoke
    output = quicksort(a_list)
    #analyze
    assert output == [1, 2, 4, 7, 10]