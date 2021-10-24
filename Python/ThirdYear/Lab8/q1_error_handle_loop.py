# Lab 7 Q1(ii)

# Looping until user provides correct value

correctValue = True

while correctValue:
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
    except ValueError:
        print("That is not a valid input")
    else:
        average = (num1 + num2) / 2
        correctValue = False
        print(f"{average:.2f}")
