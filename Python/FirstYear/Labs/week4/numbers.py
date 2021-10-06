# Corey Lynch 8/10/2019

import math

try:
    number_one = int(input("Please enter a number!"))
    number_two = int(input("Please enter one more number!"))

    if number_one == number_two:
        print("The square root of", number_one, "is", math.sqrt(number_one))

    elif number_one != number_two:
        print(number_one, "squared =", number_one**2)
        print(number_two, "squared =", number_two**2)

except ValueError:
    print("You must enter a whole number!")
