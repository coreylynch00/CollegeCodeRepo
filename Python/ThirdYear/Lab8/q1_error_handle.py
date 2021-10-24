# Lab 8 Q1

# Handling errors

def q1():
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
    except ValueError:
        print("That is not a valid input")
    else:
        average = (num1+num2)/2
        print(f"{average:.2f}")


q1()
