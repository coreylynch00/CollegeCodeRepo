# Lab 5 Q4 (i)

# For loop to print times tables

number = int(input("Enter the exponent: "))
limit = int(input("Enter the limit: "))


def tables(num, lim):
    for i in range(1, lim+1):
        print(i, "x", num, "=", i*num)


tables(number, limit)
