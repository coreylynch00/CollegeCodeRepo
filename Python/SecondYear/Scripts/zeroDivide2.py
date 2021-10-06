
def divide(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(divide(2))
print(divide(12))
print(divide(0))
print(divide(3))


