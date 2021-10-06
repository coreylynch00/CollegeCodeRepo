# Cliona McGuane
# Illustrate different error types

try:
    # ValueError: User enters a non-int
    number_of_employees = int(input("Enter number of employees: "))

    with open("employees.txt", 'w') as employee_file:
        # For each employee ask user for details and write these to the file
        for emp in range(1, number_of_employees + 1):
            print(f"Enter details for employee # {emp}")
            name = input("Name: ")
            id_number = input("ID number: ")
            dept = input("Department: ")
            print(f"{name} {id_number} {dept}", file=employee_file)
except IOError:
    print("Error creating File")
except ValueError:
    print("Integers only")

