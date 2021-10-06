try:
    feet = float(input("Feet? "))
    if feet <= 0:
        print("Data does not make sense")
    else:
        inches = feet * 12
        print(inches)
except ValueError:
    print("Bad data")