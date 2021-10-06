try:
    inches = float(input("What is the inches measurement? "))
    if inches < 0:
        print("ERROR - measurement cannot be negative")
    else:
        cm = inches * 2.54
        print(inches, "inches = ", cm , "cm")
except ValueError:
    print("ERROR - please run the program again")
