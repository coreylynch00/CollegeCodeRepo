# Corey Lynch 14/10/2019

try:
    value = int(input("Please enter a number!"))

    if 9 <= value <= 51:
        print("Valid")
    else:
        print("Invalid")

except ValueError:
    print("You must enter a number!")
