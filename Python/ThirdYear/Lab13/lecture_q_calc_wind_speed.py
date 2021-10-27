import numpy as np

data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

count = data[:, 12]

total = 0.0
for value in count:
    total += value

print("Average wind is ", total/len(count)*67)
