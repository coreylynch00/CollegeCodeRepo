# Lab 7 Q5

# Take X and Y co-ord of Cartesian system & calculate Euclidean distance

import math

x = int(input("Enter value for X co-ordinate: "))
y = int(input("Enter value for Y co-ordinate: "))

euclidean = math.hypot(x, y)

print(f"Distance = {euclidean}")
