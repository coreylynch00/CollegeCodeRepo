# number1 = float(input("Number? "))
# number2 = float(input("Divided by? "))
# result = number1 / number2
# print(result)







try:
    number1 = float(input("Number? "))
    number2 = float(input("Divided by? "))
    result = number1 / number2
    print(result)
except ValueError:
    print("That was not a number!")





try:
    number1 = float(input("Number? "))
    number2 = float(input("Divided by? "))
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("You tried to divide by zero!")
except ValueError:
    print("That was not a number!")
