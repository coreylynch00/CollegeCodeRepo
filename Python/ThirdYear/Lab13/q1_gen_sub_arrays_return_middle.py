# Lab 13 Q1

import numpy as np

arr = np.array([[1, 3, 4, 2, 3, 5], [4, 6, 4, 5, 1, 5], [3, 3, 41, 25, 1, 4]
                , [3, 3, 4, -5, 1, 4], [3, 3, 4, 5, 1, 4], [3, 3, 4, 5, 1, 4]])

print(arr)

a = int(len(arr)/3)

res = arr[a:a*2, a:a*2]

print("\n", res)
