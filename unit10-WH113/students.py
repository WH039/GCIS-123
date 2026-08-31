class Student:
    '''Student Class'''
    
    __slots__ = ['id', 'name', 'gpa', 'credits']

    def __init__ (self, id, name):
        self.id = id
        self.name = name
        self.gpa = 0
        self.credits = 0


def print_student(student):
    print("Students:", student.id + ", " + student.name + ", ", str(student.gpa) + ", ", str(student.credits))

def main():
    stu1 = Student("STU001", "Weicheng Huang")
    stu1.gpa = 4.0
    stu1.credits = 100
    print_student(stu1)

    stu2 = Student("STU002", "Adam Cross")
    stu2.gpa = 3.1
    stu2.credits = 98
    print_student(stu2)

    stu3 = Student("STU008", "Fae Rise")
    print_student(stu3)

main()