# Lab 9 Q6

# Print all unique values in a dictionary
import random

my_dict = {}

for i in range(10):
    my_dict[i+1] = random.randint(1, 20)

keys = list(my_dict.keys())
values = set(my_dict.values())

print(my_dict)
print(keys)
print(values)
