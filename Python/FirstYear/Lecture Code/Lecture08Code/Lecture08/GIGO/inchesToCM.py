try:
    inches = float(input("What is the inches measurement? "))
    cm = inches * 2.54
    print(inches, "inches = ", cm , "cm")
except ValueError:
    print("ERROR - please run the program again")
