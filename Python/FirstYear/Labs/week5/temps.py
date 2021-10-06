# Corey Lynch 14/10/2019

try:
    temp = int(input("What is the temperature today?"))

    if temp < 8:
        print("Brr, it's cold today!")
    elif 8 <= temp <= 14:
        print("It's a mild day!")
    elif 15 <= temp <= 20:
        print("It's a warm day!")
    else:
        print("It's a hot day!")
except ValueError:
    print("You must enter a whole number!")
