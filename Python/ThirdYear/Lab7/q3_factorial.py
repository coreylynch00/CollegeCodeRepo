# Lab 7 Q3

# Calculate factorial with recursion

def factorial(n):
    if n < 1:
        return 1
    else:
        return_number = n * factorial(n - 1)

    return return_number


print(factorial(5))
