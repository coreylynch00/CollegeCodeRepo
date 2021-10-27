# Lab 12 Q3 (ii)

import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])

index = np.where((a >= 5) & (a <= 10))

print(a[index])
