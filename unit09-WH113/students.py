def make_student(id, name, dictionary):
    student = [name, 0.0, 0]
    dictionary[id] = student
    

    return student

def add_student(population, id, name):
    for student in population:
        if student[0] == id:
            population.remove(student)
    new_student = make_student(id, name)
    population.append(new_student)

def get_student(population, id):
    for student in population:
        if id in student:
            return student
        
def add_credits(population, id, credits):
    student = get_student(population, id)
    student[3] += credits

def get_credits(population, id):
    student = get_student(population, id)
    return student[3]



def main():
    student_population = {}
    make_student("1002001", "Weicheng Huang", student_population)
    make_student("1002002", "Jerry Zhang", student_population)
    make_student("1002003", "Aaron Li", student_population)
    make_student("1002004", "William Ho", student_population)
    print(student_population)

    # print(population)

    # add_student(population, "1002005", "Steven Vo")
    
    # print(population)
    
    # print(get_student(population, "1002002"))

    # add_credits(population, "1002004", 3)

    # print(get_credits(population, "1002004"))

main()