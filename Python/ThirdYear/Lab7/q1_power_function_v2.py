# Lab 7 Q2

# Calculate base number after taking power number and result from user - A = B^C

import math


def power_v2(B, A):
    print("The logarithm of", A, " base on,", B, ", is: ", math.log(A, B))


def main():
    print("A = B^C")
    base = int(input("Please enter a value from B: "))
    A = int(input("Please enter a value for A: "))

    power_v2(base, A)


main()