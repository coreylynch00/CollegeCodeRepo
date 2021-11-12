# Lab 19 All Qs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from random import randint
df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")


def Q1():
    filt30l = df[df['Age'] < 30]
    filt30m = df[df['Age'] > 30]

    indexes = ['Younger 30', 'Older 30']
    population = [len(filt30l), len(filt30m)]
    plt.bar(indexes, population)
    plt.show()


def Q2():
    a1 = df['Age'] < 30
    a2 = df['Age'] > 30

    a3 = df['Sex'] == 'male'
    a4 = df['Sex'] == 'female'

    Mfilt30l = df[a1 & a3]

    Mfilt30m = df[a2 & a3]

    Ffilt30l = df[a1 & a4]
    Ffilt30m = df[a2 & a4]

    labels = ['Younger 30', 'Older 30']

    indexes = np.arange(1, 3)
    Mpopulation = [len(Mfilt30l), len(Mfilt30m)]
    Fpopulation = [len(Ffilt30l), len(Ffilt30m)]
    bar_width = 0.35

    plt.bar(indexes, Mpopulation, bar_width)
    plt.bar(indexes + bar_width, Fpopulation, bar_width)
    plt.xticks(indexes + 0.2, labels)
    plt.legend(['Male', 'Female'])
    plt.show()


def Q3():
    dd = df[['Age', 'Fare']].dropna()
    print(dd)
    area = np.pi * (np.random.rand() * 1)
    plt.scatter(dd['Age'], dd['Fare'], s=area, color='r')
    plt.show()


def Q4():
    ages = df['Age'].dropna()
    plt.hist(ages, bins=40)
    plt.title("Age distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()


def Q5_i():
    fares = df['Fare'].dropna()
    plt.boxplot(fares)
    plt.xlabel("Fare")
    plt.show()


def Q5_ii():
    fares = df['Age'].dropna()
    plt.boxplot(fares)
    plt.xlabel("Age")
    plt.show()


def Q6():
    a1 = df[df['Age'] < 25]
    b1 = df['Age'] >= 25
    b2 = df['Age'] < 50
    a2 = df[b1 & b2]
    b1 = df['Age'] >= 50
    b2 = df['Age'] < 75
    a3 = df[b1 & b2]
    a4 = df[df['Age'] >= 75]
    ages = [len(a1), len(a2), len(a3), len(a4)]
    labels = ['< 25', '25 to 50', '50 to 75', '> 75']
    sectionToExplode = (0.1, 0, 0, 0)
    plt.pie(ages, shadow=True, startangle=90, autopct='%0.1f%%', pctdistance=1.1, labeldistance=1.3, labels=labels)
    # plt.legend(patches, labels, loc="best")
    plt.annotate('The largest age cluster', xy=(1, 0.5), xytext=(1, 2),
                 arrowprops=dict(arrowstyle="->"))

    plt.show()
