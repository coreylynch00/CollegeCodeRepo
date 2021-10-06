from math import sqrt

SQUARE_ROOT_SYMBOL = "\u00B2"

file = open("numbers.txt")
squares_file = open("squares.txt", "w")
for line in file:
    number = float(line)
    square = number**2
    squares_file.write("{}\u00B2 "
                       "= {:.4f}\n"
                       .format(number, square))
file.close()
squares_file.close()