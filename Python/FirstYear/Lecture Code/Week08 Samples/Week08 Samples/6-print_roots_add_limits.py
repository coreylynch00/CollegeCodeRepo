import math

SQUARE_ROOT_SYMBOL = "\u221A"
startVal = int(input("Please enter lowest value: "))
endVal = int(input("Please enter highest value: "))

for i in range(startVal, endVal + 1):
    print("{}{} = {:.6f}".format(SQUARE_ROOT_SYMBOL, i, math.sqrt(i)))

