number = int(input("Please type a number "))
if number > 0 and number % 2 == 0:
    ok = True
else:
    ok = False

if not ok:
    print("Houston we have a problem!")
