# Lab 9 Q1

# Ask user for name & StudentID and store in dict. Check if ID is unique


def student_dict():
    students = {}
    cont = 'y'

    while cont == 'y':
        name = input("Please enter your name: ")
        student_id = input("Please enter you Student ID: ")
        if student_id in students:
            print("This student ID is already taken!")
        else:
            students[name] = student_id
        cont = input("Do you want to continue? [y/n]: ")
    print(students)


student_dict()

