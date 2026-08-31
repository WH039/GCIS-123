# advanced_plots.py by Weicheng Huang
#library
import csv
import plotter

#constants


#functions
def plot_grades(filename, firstname, lastname):
    student_name = firstname + " " +lastname
    with open(filename) as file:
        next(file)
        reader = csv.reader(file)
        for record in reader:
            if record[0] == lastname and record[1] == firstname: 
                plotter.init(student_name, "Grade Item", "Score")
                index = 3
                plotter.new_series("Grades")
                while index < len(record):
                    try:
                        plotter.add_data_point(float(record[index]))
                        index += 1
                    except ValueError:
                        plotter.add_data_point(0.0)
                        index += 1
                plotter.plot()
            else:
                continue

def get_average(filename, column):
    sum_avg = 0.0
    index = 0
    with open(filename) as a_file:
        next(a_file)
        reader = csv.reader(a_file)
        for record in reader:
            try:
                sum_avg += float(record[column])
                index += 1
            except ValueError:
                index += 1
        
    avg = sum_avg / index
    
    return avg

def plot_class_average(filename):
    index = 3
    plot_title = "Class Average (" + filename + ")"
    plotter.init(plot_title, "Average", "Grade Item")
    plotter.new_series(filename)
    while index < 30:
        plotter.add_data_point(get_average(filename, index))
        index += 1
    plotter.plot()

#main

def main():
    #plot_grades("data/grades_010.csv", "Endre", "Foell")
    plot_class_average("data/full_grades_999.csv")

main()