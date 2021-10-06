number = int(input("Please type a number > "))
remainder = number % 2
if remainder == 0:
    print(str(number) + " is even.")
else:
    print(str(number) +  " is odd.")