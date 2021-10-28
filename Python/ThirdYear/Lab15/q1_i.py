# Lab 15 1 (i)

import numpy as np

data = np.genfromtxt('bikeSharing.csv', delimiter=',')


def compareHolidays(data, holiday):

    subset = data[data[:, 5] == holiday]

    print("Number of entries ", len(subset))

    print("Mean", np.mean(subset[:, 15]))


compareHolidays(data, 0)
compareHolidays(data, 1)
