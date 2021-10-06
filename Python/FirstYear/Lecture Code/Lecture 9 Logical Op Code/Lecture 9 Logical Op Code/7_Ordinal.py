
number = int(input("What day?"))

if number % 10 == 1 and number % 100 != 11 :
    print(str(number) + "st")
elif number % 10 == 2 and number % 100 != 12 :
    print(str(number) + "nd")
elif number % 10 == 3 and number % 100 != 13:
    print(str(number) + "rd")
else:
    print(str(number) + "th")
    

