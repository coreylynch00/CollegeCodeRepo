# Read numbers from a file
with open("numbers.txt") as numbers:
    for line in numbers:
        number = float(line)
        print(number)
