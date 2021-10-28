# Lab 15 Q1 (iv)

import numpy as np


def averageNumRentalBikesPerCondition(data):
    conditions = {1: "Clear", 2: "Misty", 3: "Light Rain", 4: "Heavy Rain"}

    for key in conditions:
        subsetData = data[data[:, 8] == key]

        print(np.mean(subsetData[:, 15]))


def main():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')

    averageNumRentalBikesPerCondition(data)


main()
