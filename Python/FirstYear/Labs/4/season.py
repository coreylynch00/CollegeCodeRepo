# Corey Lynch 10/10/2019
try:
    season = int(input("Please enter a number 1 - 4 to calculate the season!"))
    if season == 1:
        print("It's Winter!")
    elif season == 2:
        print("It's Spring!")
    elif season == 3:
        print("It's Summer!")
    elif season == 4:
        print("It's Autumn!")
    else:
        print("ERROR: You must choose a value you between 1 and 4!")
except ValueError:
    print("ERROR: You must enter a number between 1 - 4!")

