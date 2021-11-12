# Lab 16 All Qs

import pandas as pd
import numpy as np


def Q1_i():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    locs = df['Location'].value_counts()
    print(type(locs))
    print(locs.head(1))


def Q1_ii():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    locs = df['Country'].value_counts()
    print(type(locs))
    print(locs.head(6))


def Q1_iii():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    criteria1 = df["Fatal"] == 'Y'
    countries_fatal = df[criteria1]
    locs = countries_fatal['Country'].value_counts()

    print(locs.head(6))


def Q1_iv():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    boolSurfAttacks = df["Activity"] == "Surfing"
    boolScubaAttacks = df["Activity"] == "Scuba diving"

    print("Number of attacks when surfing ", len(df[boolSurfAttacks]))
    print("Number of attacks when Scuba Diving ", len(df[boolScubaAttacks]))


def Q2_i():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    criteria1 = df["Fatal"] == 'Y'
    countries_fatal = df[criteria1]
    print(len(countries_fatal) * 100 / len(df))


def Q2_ii():
    df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
    countries = pd.unique(df["Country"])
    for c in countries:
        country = df['Country'] == c
        fatal = df["Fatal"] == 'Y'
        Non_Fatal = df["Fatal"] == 'N'

        country_fatal = df[country & fatal]
        country_Non_Fatal = df[country & Non_Fatal]
        if len(country_fatal) > 0:
            print('The percentage of fatal attacks: ', c,
                  len(country_fatal) * 100 / (len(country_fatal) + len(country_Non_Fatal)))

        # Q3


def yearlyAttack(c, df):
    countryBool = df['Country'] == c

    for yr in pd.unique(df['Year']):
        if yr > 1924 and yr < 2016:
            yeahBool = df['Year'] == yr
            countryYear = df[countryBool & yeahBool]
            print()
            print(c, yr, len(countryYear))


Q1_i()