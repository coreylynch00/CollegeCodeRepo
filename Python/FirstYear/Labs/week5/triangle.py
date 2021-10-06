# Corey Lynch 14/10/2019

try:
    side_one = float(input("Enter the length of the first side."))
    side_two = float(input("Enter the length of the second side."))
    side_three = float(input("Enter the length of the third side"))

    if side_one == side_two and side_two == side_three:
        print("It is equilateral.")
    elif side_one == side_two or side_two == side_three or side_one == side_three:
        print("It is isosceles.")
    else:
        print("It is scalene.")
except ValueError:
    print("You must enter a number.")
