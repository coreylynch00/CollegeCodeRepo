# Lab 15 Q1 (ii)

import numpy as np

data = np.genfromtxt('bikeSharing.csv', delimiter=',')

newdata = np.copy(data)

print(newdata[:, 9])

newdata[:, 9] *= 41

print(newdata[:, 9])
