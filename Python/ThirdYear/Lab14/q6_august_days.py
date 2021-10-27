# Lab 14 Q6

import numpy as np

days = np.array([])
for i in range(1, 32):
    days = np.append(days, i)

even_days = days[days % 2 == 0]
print(even_days)
