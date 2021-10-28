# Lab 15 Q1 (iii)

import numpy as np

data = np.genfromtxt('bikeSharing.csv', delimiter=',')

result = data[:, 13] > data[:, 14]

print("Percentage of time where causal users > registered: ", (len(data[result])*100.0)/len(data))
