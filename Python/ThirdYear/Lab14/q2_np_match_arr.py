# Lab 14 Q2

import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 6])


def match(arr_a, arr_b):
    c = np.where(arr_a == arr_b)
    arr_b[c] = -1
    print(arr_b)


match(a, b)
