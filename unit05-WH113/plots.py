# Assignment 5.1 by Weicheng Huang

#libraries
import plotter

#constants


#functions
def terminate():
    quit = input("Are you sure you want to quit? (y/n): ")
    if quit == 'y' or quit == 'Y':
        return True
    elif quit == 'n' or quit == 'N':
        return False

def plot_grades(filename, firstname, lastname):
    student_name = firstname + " " +lastname
    found = False
    with open(filename) as file:
        next(file)
        for line in file:
            student = line.split(',')
            if student[0] == lastname and student[1] == firstname: 
                found == True
                plotter.init(student_name, "Grade Item", "Score")
                index = 3
                plotter.new_series("Grades")
                while index < len(student):
                    try:
                        plotter.add_data_point(float(student[index]))
                        index += 1
                    except ValueError:
                        plotter.add_data_point(0.0)
                        index += 1
                plotter.plot()
                return True
            else:
                continue
        if found == False:
            return False

def student_grades(filename=None, firstname=None, lastname=None):
    if not filename or not firstname or not lastname:
        print("Usage: stu <filename> <first name> <last name>")
    else:
        try:
            student_found = plot_grades(filename, firstname, lastname)
            if student_found == True:
                print("Plot finished")
            else:
                print("Plot failed (no such student).")
        except FileNotFoundError:
            print("No such file:", filename)        

#main
def main():
    while True:
        cmd = input(">> ")
        cm = cmd.split(' ')
        if cm[0] == "quit":
            if terminate() == True:
                print("Goodbye")
                break
        if cm[0] == '':
            print("Enter a command or 'quit' to quit.")
        if cm[0] == "stu":
            if len(cm) == 1:
                student_grades()
            else:
                student_grades(cm[1], cm[2], cm[3])
        if cm[0] == "help":
            print("stu <filename> <first name> <last name> - plot student grades")
            print("quit - quits")
            print("help - displays this message")

main()