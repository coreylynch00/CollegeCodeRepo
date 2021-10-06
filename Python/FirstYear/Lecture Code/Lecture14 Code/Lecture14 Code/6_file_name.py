
try:
    number_of_employees = int(input("Enter number of employees: "))

    with open("employees.txt", 'w') as employee_file:
        for emp in range(1, number_of_employees + 1):
            print(f"Enter details for employee # {emp}")
            name = input("Name: ")
            id_number = input("ID number: ")
            dept = input("Department: ")
            print(f"{name} {id_number} {dept}", file=employee_file)

    print("The data can be found in {}.".format(employee_file.name))

except IOError:
    print("Error creating File {}".format(employee_file.name))
except ValueError:
    print("Some other error")


