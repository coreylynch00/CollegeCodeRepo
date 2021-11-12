# Lab 18 All Qs

import pandas as pd
import numpy as np
#import datetime as DT
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

def Q1():
    X = range(1, 50)
    Y = [value * 3 for value in X]
    print("Values of X:")
    print(range(1, 50))
    print("Values of Y (thrice of X):")
    print(Y)
    # Plot lines and/or markers to the Axes.
    plt.plot(X, Y)
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Set a title
    plt.title('Draw a line.')
    # Display the figure.
    plt.show()


def Q2():
    # x axis values
    x = [1, 2, 3]
    # y axis values
    y = [2, 4, 1]
    # Plot lines and/or markers to the Axes.
    plt.plot(x, y)
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Set a title
    plt.title('Sample graph!')
    # Display a figure.
    plt.show()


def Q3():
    df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
    df.plot()
    print(df.index)
    plt.show()


def Q4():
    x1 = [10, 20, 30]
    y1 = [20, 40, 10]
    # line 2 points
    x2 = [10, 20, 30]
    y2 = [40, 10, 30]
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Plot lines and/or markers to the Axes.
    plt.plot(x1, y1, color='blue', linewidth=3, label='line1-dotted', linestyle='dotted')
    plt.plot(x2, y2, color='red', linewidth=5, label='line2-dashed', linestyle='dashed')
    # Set a title
    plt.title("Plot with two or more lines with different styles")
    # show a legend on the plot
    plt.legend()
    # function to show the plot
    plt.show()


def Q5():
    # Sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # green dashes, blue squares and red triangles
    plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
    plt.show()


def Q6():
    df = pd.read_csv("titanic.csv", encoding="ISO-8859-1")
    criteria = df['Survived'] == 1
    survived = df[criteria]
    pclassGroup = survived.groupby("Pclass")

    classSurived = pclassGroup['Survived'].count()
    print(classSurived)
    classSurived.plot()
    plt.show()


def Q7():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = np.arange(0, 6)
    plt.bar(x_pos, popularity, color='blue')
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)
    # Turn on the grid
    plt.minorticks_on()
    plt.show()


def Q8_a():
    df = pd.read_csv("titanic.csv", encoding="ISO-8859-1")
    ndf = df[['Survived', 'Sex']]
    ndf1 = ndf['Survived'] == 1
    ndf2 = ndf['Survived'] == 0

    ndf11 = ndf[ndf1]

    ndf22 = ndf[ndf2]

    index = np.arange(1, 3)

    plt.bar(index, ndf11['Sex'].value_counts(), 0.2)

    plt.bar(index + 0.2, ndf22['Sex'].value_counts(), 0.2)

    plt.xticks(index, ['Male', 'Female'])
    plt.legend(['Survived', 'died'])
    plt.show()


def Q8_b():
    df = pd.read_csv("titanic.csv", encoding="ISO-8859-1")
    ndf = df[['Age', 'Sex']]
    l1 = ndf['Age'] < 40
    l2 = ndf['Age'] > 20
    ndf = ndf[l1 & l2]

    print(ndf)

    index = np.arange(1, 3)
    plt.xticks(index, ['Male', 'Female'])
    print(ndf['Sex'].value_counts())
    plt.bar(index, ndf['Sex'].value_counts(), 0.2)
    plt.show()


def Q8_c():
    df = pd.read_csv("titanic.csv", encoding="ISO-8859-1")
    ndf = df[['Pclass', 'Fare']]
    pclassGroup = ndf.groupby("Pclass").mean()

    print(pclassGroup)
    index = [1, 2, 3]

    plt.bar(index, pclassGroup['Fare'])
    plt.xticks(index, ['first', 'second', 'third'])
    plt.show()


def Q8_d():
    df = pd.read_csv("titanic.csv", encoding="ISO-8859-1")
    clss = df['Pclass']

    population = clss.value_counts()
    print(population)
    labels = ['Third', 'First', 'Second']
    plt.pie(population, autopct='%1.1f%%', labels=labels)
    plt.show()
