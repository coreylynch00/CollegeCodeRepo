# Lab 14 Q3

import numpy as np

arr = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])

index = np.where((arr >= 5) & (arr <= 10))

print(arr[index])
