# Lab 13 Q3 (ii)

import numpy as np

myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

print("Min: ", np.min(myfile[:, 9]))
print("Max: ", np.max(myfile[:, 9]))
print("Mean: ", np.mean(myfile[:, 9]))
