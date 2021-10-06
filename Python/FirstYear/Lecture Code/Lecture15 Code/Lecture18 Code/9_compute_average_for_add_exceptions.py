# Reads in a file, loops through its contents with WHILE loop and
# computes the average of the numbers in the file

# Extras: Checks for IO, Value and ZeroDivision errors

try:
    counter = 0
    running_total = 0
    with open("numbers.txt") as numbers_file:
        for line in numbers_file:
            running_total = running_total + float(line)
            counter = counter + 1
        average = running_total / counter
        print("Average is {:.4f}".format(average))
except ValueError:
    print(f"Could not convert '{line.rstrip()}' into a floating point number")
except IOError as err: # or FileNotFoundError
    print("Could not find file\n\t", err)
except ZeroDivisionError:
    print("File", numbers_file.name, "didn't contain any values")
except:
    print("Error")
