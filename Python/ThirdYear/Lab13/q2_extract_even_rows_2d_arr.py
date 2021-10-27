# Lab 13 Q2
import numpy as np

arr = np.array([[1, 3, 4, 2, 3, 5], [4, 6, 4, 5, 1, 5], [3, 3, 41, 25, 1, 4]

                , [3, 3, 4, -5, 1, 4], [3, 3, 4, 5, 1, 4], [3, 3, 4, 5, 1, 4]])

a = int(len(arr[0]) / 2)

print(arr[1:: 2, a:])  # col with indexes: 1,3,5,7,9,… and print second half of col
print("\n")
print(arr[:: 2, a:])  # col with indexes: 0,2,4,6,8,… and print second half of col
