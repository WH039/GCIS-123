# Assignment 6.2
# Weicheng Huang

# libraries
import arrays
import plotter
import time
import searches

# functions
def average_binary_search(size):
    an_array = arrays.Array(size)
    array_range = range(size)
    index = 0
    while index < len(an_array):
        an_array[index] = index
        index += 1

    total_time = 0
    for index in array_range:
        start = time.perf_counter()
        searches.binary_search(an_array, index)
        end = time.perf_counter()
        total_time += (end - start)
    
    average_time = total_time / len(an_array)
    return average_time

def plot_average_binary_search(min_size, max_size, runs):
    a_range = range(min_size, max_size, runs)
    plotter.new_series("Binary")
    for int in a_range:
        plotter.add_data_point(average_binary_search(int))
    return

def average_trinary_search(size):
    an_array = arrays.Array(size)
    array_range = range(size)
    index = 0
    while index < len(an_array):
        an_array[index] = index
        index += 1

    total_time = 0
    for index in array_range:
        start = time.perf_counter()
        searches.trinary_search(an_array, index)
        end = time.perf_counter()
        total_time += (end - start)
    
    average_time = total_time / len(an_array)
    return average_time

def plot_average_trinary_search(min_size, max_size, runs):
    a_range = range(min_size, max_size, runs)
    plotter.new_series("Trinary")
    for int in a_range:
        plotter.add_data_point(average_trinary_search(int))
    return

def plot_average_search(min_size, max_size, runs):
    a_range = range(min_size, max_size, runs)
    plotter.init("Search Average", "Size", "Time")
    plotter.new_series("Binary")
    for int in a_range:
        plotter.add_data_point(average_binary_search(int))
    plotter.new_series("Trinary")
    for int in a_range:
        plotter.add_data_point(average_trinary_search(int))
    plotter.plot()
    return
# main
def main():

    plot_average_search(100, 10000, 25)
    plotter.init("Binary Search", "Size", "Time")
    plot_average_binary_search(100, 10000, 25)
    plotter.plot()
    plotter.init("Trinary Search", "Size", "Time")
    plot_average_trinary_search(100, 10000, 25)
    plotter.plot()

main()