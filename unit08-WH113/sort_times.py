import sorts
import plotter
import time

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def sort_functon_timer(a_list, sort_function):
    start = time.perf_counter()
    sort_function(a_list)
    end = time.perf_counter()

    return end - start

def plot_sort_time_using_random_lists(sort_function):
    plotter.new_series(sort_function.__name__)
    for value in SIZES:
        temp_list = sorts.random_list(value)
        elapsed_time = sort_functon_timer(temp_list, sort_function)
        plotter.add_data_point(elapsed_time)

def plot_sort_time_using_sorted_lists(sort_function):
    plotter.new_series(sort_function.__name__)
    for value in SIZES:
        temp_list = list(range(0, value))
        elapsed_time = sort_functon_timer(temp_list, sort_function)
        plotter.add_data_point(elapsed_time)

def main():
    # a_list1 = list(range(1,3001))
    # a_list2 = list(range(1,3001))
    # a_list3 = list(range(1,3001))

    # b_list1 = sorts.random_list(3000)
    # b_list2 = sorts.random_list(3000)
    # b_list3 = sorts.random_list(3000)
    
    # c_list1 = list(range(3000, 0, -1))
    # c_list2 = list(range(3000, 0, -1))
    # c_list3 = list(range(3000, 0, -1))

    # print(insertion_sort_functon_timer(a_list, sorts.insertion_sort), "seconds.")
    # print(insertion_sort_functon_timer(b_list, sorts.insertion_sort), "seconds.")
    # print(insertion_sort_functon_timer(c_list, sorts.insertion_sort), "seconds.")

    # print(insertion_sort_functon_timer(a_list, sorts.insertion_sort_wo_swap), "seconds.")
    # print(insertion_sort_functon_timer(b_list, sorts.insertion_sort_wo_swap), "seconds.")
    # print(insertion_sort_functon_timer(c_list, sorts.insertion_sort_wo_swap), "seconds.")

    # print("Insertion Sort sorted: ", insertion_sort_functon_timer(a_list1, sorts.insertion_sort), sep='')
    # print("Insertion Sort random: ", insertion_sort_functon_timer(b_list1, sorts.insertion_sort), sep='')
    # print("Insertion Sort reverse: ", insertion_sort_functon_timer(c_list1, sorts.insertion_sort), sep='')

    # print("Insertion Sort (wo) sorted: ", insertion_sort_functon_timer(a_list2, sorts.insertion_sort_wo_swap), sep='')
    # print("Insertion Sort (wo) random: ", insertion_sort_functon_timer(b_list2, sorts.insertion_sort_wo_swap), sep='')
    # print("Insertion Sort (wo) reverse: ", insertion_sort_functon_timer(c_list2, sorts.insertion_sort_wo_swap), sep='')

    # print("Bubble Sort sorted: ", insertion_sort_functon_timer(a_list3, sorts.bubble_sort), sep='')
    # print("Bubble Sort random: ", insertion_sort_functon_timer(b_list3, sorts.bubble_sort), sep='')
    # print("Bubble Sort reverse: ", insertion_sort_functon_timer(c_list3, sorts.bubble_sort), sep='')

    plotter.init("Insetion and Merge Sort(random)", "Array Size", "Time")
    plot_sort_time_using_random_lists(sorts.insertion_sort)
    plot_sort_time_using_random_lists(sorts.merge_sort)
    plot_sort_time_using_random_lists(sorts.quicksort)
    plotter.plot()
    plotter.init("Insetion and Merge Sort(sorted)", "Array Size", "Time")
    plot_sort_time_using_sorted_lists(sorts.insertion_sort)
    plot_sort_time_using_sorted_lists(sorts.merge_sort)
    plot_sort_time_using_sorted_lists(sorts.quicksort)
    plotter.plot()

    '''
    Assignemnt 8.2, Part 3:
    Could nto complete due to an error with matplotlib, I tried reinstalling but still ran into the same issue
    Older modules with plotter worked fine so this seems to be isolated to this unit

    Using sorted lists will cause an recursion limit error as in a sorted list quicksort will attempt to do every value. Which with a recursion limit of ~1000 will trip an error past size 800

    Assignment 8.2, Part 5:
    As stated before I could not use plotter as the the matplotlib problem persisted
    All code is completed, but could not verify result
    '''

main()