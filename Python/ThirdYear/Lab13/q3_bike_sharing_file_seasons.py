# Lab 13 Q3 (i)

import numpy as np

myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')
print(set(myfile[:, 1]))


myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')
print(np.unique(myfile[:, 1]))
