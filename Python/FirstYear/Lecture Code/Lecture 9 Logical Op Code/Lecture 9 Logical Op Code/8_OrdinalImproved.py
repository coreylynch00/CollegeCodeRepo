try:
    number = int(input("What day?"))

    # to save Python calculating this repeatedly
    # I calculate it once and store it
    lastDigit = number % 10
    # ditto the last 2 digits
    last2Digits = number % 100

    if lastDigit == 1 and last2Digits != 11:
        print(str(number) + "st")
    elif lastDigit == 2 and last2Digits != 12:
        print(str(number) + "nd")
    elif lastDigit == 3 and last2Digits != 13:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
except:
    print("Error - please try again.")

