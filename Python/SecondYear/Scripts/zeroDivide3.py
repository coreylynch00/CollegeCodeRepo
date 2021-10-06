
def divide(divideBy):
    return 42 / divideBy

try:
    print(divide(2))
    print(divide(12))
    print(divide(0))
    print(divide(3))

except ZeroDivisionError:
    print("Error: Invalid argument.")


