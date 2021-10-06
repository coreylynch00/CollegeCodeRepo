import math
SQUARE_ROOT_SYMBOL = "\u221A"
while True:
    try:
        startVal = int(input("Please enter lowest value: "))
        endVal = int(input("Please enter highest value: "))
        if startVal < endVal:
            break
        else:
            print("Input error, lowest value must be less than highest value")
    except ValueError:
        print("Input error, must enter integers.")

for i in range(startVal, endVal + 1):
    print("{}{} = {:.6f}".format(SQUARE_ROOT_SYMBOL, i, math.sqrt(i)))