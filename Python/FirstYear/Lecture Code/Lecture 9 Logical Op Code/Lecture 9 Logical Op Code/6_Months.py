month = int(input("What month? "))

if month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 2:
    print("28 days")
else:
    print("31 days")