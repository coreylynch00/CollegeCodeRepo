# quadratic3.py
#    A program that computes the real roots of a quadratic equation.

import math

print("This program finds the real solutions to a quadratic\n")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discrim = b * b - 4 * a * c
if discrim > 0:
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("The solutions are:", root1, root2)
elif discrim == 0:
    root = -b / (2 * a)
    print("There is a double root at", root)
else:
    print("There are no real roots")
