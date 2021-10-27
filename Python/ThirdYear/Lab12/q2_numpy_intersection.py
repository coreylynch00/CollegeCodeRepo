# Lab 12 Q2
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])


def intersect(arr_a, arr_b):
    # Find intersection
    intrsect = np.intersect1d(arr_a, arr_b)
    print(f"\nA = {arr_a}\nB = {arr_b}")
    print(f"Intersection = {intrsect}")

    # Remove intersection from A
    rem_int_a = np.setdiff1d(arr_a, arr_b)
    print(f"A Without Intersection = {rem_int_a}")


intersect(a, b)