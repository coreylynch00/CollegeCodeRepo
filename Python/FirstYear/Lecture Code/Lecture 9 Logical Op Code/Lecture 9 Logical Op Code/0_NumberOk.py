number = int(input("Please type a number "))

ok = number > 0 and number % 2 == 0

if not ok:
    print("Houston we have a problem!")