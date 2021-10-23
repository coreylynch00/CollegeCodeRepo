# Lab 9 Q3

# Merge dictionaries

first = {"Corey": 1, "Mollie": 2}
second = {"Bob": 3, "Joe": 4}

# def merge(x, y):
#    z = x.copy()
#    z.update(y)
#    print(z)
# merge(first, second)

first.update(second)
print(first)
