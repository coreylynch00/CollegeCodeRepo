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
    black_white = df[df['color'].str.strip() == 'Black and White']
    grp = black_white.groupby('actor_1_name')['color']
    for name, dataf in grp:
        print(name)
        print(dataf, "\n")
    print(len(grp))


def Task2():
    cond = df[df['language'] != 'English']
    grp = cond.groupby('country')['language']
    for count, lang in grp:
        print(count)
        print(lang, "\n")


def Task3():    # Complete
    mean = df['gross'].mean()
    # print(mean)   # = 48468407.52680933
    df['gross'] = df['gross'].fillna(mean)
    grp = df.groupby('title_year')['gross']
    total = (grp.sum() / 1000000000)    # Dividing by 1 billion to make numbers more eligible
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
    cond = df[(df.title_year > 1989) & (df.gross > df.budget)]
    print(cond)

#def Task5():


#def Task6():
    

#Task1()
#Task2()
#Task3()
Task4()