# Lab 14 Q1

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])


def intersect_arr(arr_a, arr_b):
    c = np.intersect1d(arr_a, arr_b)
    print(c)
    

intersect_arr(a, b)
