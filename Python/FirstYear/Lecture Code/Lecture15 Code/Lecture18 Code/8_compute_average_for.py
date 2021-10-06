# compute_average_for1.py
# Reads in a file, loops through its contents with FOR loop and computes the average of the numbers in the file

# initialise counter and average_value variables
counter = 0
running_total = 0

with open("numbers.txt") as numbers_file:
    for line in numbers_file:
        running_total = running_total + float(line)
        counter = counter + 1
    average = running_total / counter
    print(f"Average is {average:.4f}")


