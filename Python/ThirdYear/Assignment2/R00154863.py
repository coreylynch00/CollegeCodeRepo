# -*- coding: utf-8 -*-
"""
Created on a cloudy day

@author: Corey Lynch
@id: R00154863
@Cohort: SD3-B
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
# print(len(df))


def Task1():
    # Cleanse data and extract movies that are Black and White
    black_white = df[df['color'].str.strip() == 'Black and White']
    # Group by actor name and include the movie title
    grp = black_white.groupby('actor_1_name')['movie_title']
    # Print Actor Name and the corresponding Movie Title of that Black and White movie
    for name, mov in grp:
        print(name)
        print(mov, "\n")
    # print(len(grp))


def Task2():
    # New dataframe where language is not English and duration is greater than 150 minutes
    cond = df[(df.language != 'English') & (df.duration > 150)]
    # Group by country and include the movie duration and title
    grp = cond.groupby(['country', 'language'])['movie_title']
    # Print Country and Language and corresponding Movie Title of the criteria
    for count, dur in grp:
        print(count)
        print(dur, "\n")


def Task3():
    # Calculate mean
    mean = df['gross'].mean()
    # print(mean)   # = 48468407.52680933
    df['gross'] = df['gross'].fillna(mean)
    grp = df.groupby('title_year')['gross']
    total = (grp.sum() / 1000000000)    # Dividing by 1 billion to make numbers more legible
    print(total)     # Empty cells now contain 0.048468 (mean / 1000000000) = $48,468,000
    # print(total * 1000000000)   # Returns total back to default values (base 10)

    # Plot graph
    plt.plot(total, marker='.')
    plt.title("Income Per Annam")
    plt.xlabel("Year")
    plt.ylabel("Income (In Billions)")
    plt.legend(['Income That Year'], loc="upper left")
    plt.show()


def Task4():
    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
    cond1 = df[(df.title_year > 1989)]
    cond2 = cond1[(df.gross > (df.budget * 2))]
    grp1 = cond1.groupby('title_year').size()
    # for year in grp1:
    #    print(year)
    grp2 = cond2.groupby('title_year').size()
    # for year in grp2:
    #    print(year)
    # Calculate percentage
    percent = (grp2 / grp1) * 100
    print(percent)

    # Plot graph
    plt.plot(percent, marker='.')
    plt.title("Percentage of movies where income is higher than double the budget")
    plt.xlabel("Year")
    plt.ylabel("Percent")
    plt.show()


def Task5():
    drop1 = df[(df['country'] == 'USA') | (df['country'] == 'UK')].index
    df.drop(drop1, inplace=True)
    # print(len(df))
    grp = df.groupby('country').filter(lambda x: x['movie_title'].count() < 30)
    # print(len(grp))
    grp2 = grp.groupby('country').size()
    # for count in grp2:
    #    print(count)
    grp2.plot.bar()
    plt.show()


def Task6():
    # Data cleansing
    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
    # print(len(df))
    grp = df.groupby('duration')['movie_title'].count()

    # Plot graph
    grp.plot()
    plt.style.use('seaborn-whitegrid')
    plt.title("Graph demonstrating common movie durations")
    plt.xlabel("Duration (In Minutes)")
    plt.ylabel("Number of Movies with Duration")
    plt.show()


#Task1()
#Task2()
#Task3()
#Task4()
#Task5()
#Task6()
