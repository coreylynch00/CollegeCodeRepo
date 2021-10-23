# Lab 9 Q5

# Create dict with for loop, generate random keys and convert to 2 lists

import random

my_dict = {}

for i in range(11):
    my_dict[i + 1] = random.randint(1, 20)

keys = list(my_dict.keys())

values = list(my_dict.values())

print(my_dict)
print(keys)
print(values)

