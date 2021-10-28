# Lab 15 Q1 (v)

import numpy as np


def main():
    data = np.genfromtxt('bikeSharing.csv', delimiter=',')

    for temp in range(1, 40, 5):
        analyseTemp(data, temp, temp + 4)


def analyseTemp(data, minValue, maxValue):
    # the temperature values stored in the array are multiplied by 41

    higherTempCondition = (data[:, 9] * 41) >= minValue

    lowerTempCondition = (data[:, 9] * 41) <= maxValue

    subset = data[higherTempCondition & lowerTempCondition]

    meanValue = np.mean(subset[:, 13])

    print("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)


main()
