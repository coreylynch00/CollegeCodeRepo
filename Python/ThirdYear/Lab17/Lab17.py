# Lab 17 All Qs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.dates import date2num


def Q1_i():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")

    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')

    grs = df.groupby('Country')['Age'].mean()
    print(grs)


def Q2():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def Q3():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        cn = cn.dropna(subset=['Area'])
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def Q4():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    fatals = df[df['Fatal'] == 'Y']
    grs = fatals.groupby('Country')['Fatal'].size()
    print(grs)


def Q5():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")

    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=['Age'])

    yrs = df.groupby('Year')
    averg = yrs['Age'].mean()
    # averg = averg.dropna()

    print(averg.sort_values().tail(10))

