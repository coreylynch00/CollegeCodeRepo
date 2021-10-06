number = int(input("Please type a number > "))
even = number % 2 == 0
if even:
    print(str(number) + " is even.")
else:
    print(str(number) +  " is odd.")