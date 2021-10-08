# Lab 5 Q4 (ii)

# Loop to print number triangle

size = int(input("Enter an integer for triangle size: "))


def print_num_triangle(x):
    for i in range(x+1):
        for j in range(i):
            print(i, end=' ')
        print('')


print_num_triangle(size)
