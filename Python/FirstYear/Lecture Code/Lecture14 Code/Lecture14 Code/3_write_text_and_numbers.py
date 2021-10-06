# Author: Cliona McGuane
# Demonstrate writing mixed data to a file
name= 'Fred'
age = 21
average_grade = 56.7

with open("output.txt", 'w') as output_file:
    print("Welcome to my file.", file=output_file)
    print(f"{name} is {age} years old.", file=output_file)
    print(f"{name} has an average grade of {average_grade:.3f}", file=output_file)

output_file.close()
