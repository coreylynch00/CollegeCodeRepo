#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on a windy day

@author: Corey Lynch
@id: R00154863
@Cohort: SD3-B
"""

from sklearn import datasets, model_selection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rnd
from sklearn import datasets
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import cross_validate
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import KBinsDiscretizer

df = pd.read_csv("weatherAUS.csv", encoding='utf8')

# print(df.shape)

def Task1():

    """
    *** NOTE : You must exit out of each graph to generate the next! ***
    """

    subDF = df[['MinTemp', 'WindGustSpeed', 'Rainfall', 'RainTomorrow']]

    df_clean = subDF.dropna()
    # print(df_clean.shape)

    featureColsA = df_clean[['MinTemp', 'WindGustSpeed', 'Rainfall']]
    # print(featureColsA)

    featureColsB = df_clean[['MinTemp', 'WindGustSpeed']]
    # print(featureColsB)

    featureColsC = df_clean[['MinTemp', 'Rainfall']]
    # print(featureColsC)

    featureColsD = df_clean[['WindGustSpeed', 'Rainfall']]
    # print(featureColsD)

    y = df_clean.RainTomorrow
    # print(y)

    max_depth_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                      22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    accuracy_listA = []
    accuracy_listB = []
    accuracy_listC = []
    accuracy_listD = []

############################### FEATURE COLS A ######################################

    Xa = featureColsA
    # print(Xa)

    Xa_train, Xa_test, y_train, y_test = train_test_split(Xa, y, test_size=0.33)

    for x in max_depth_list:
        clf = tree.DecisionTreeClassifier(max_depth=x, random_state=1)
        clf.fit(Xa_train, y_train)
        y_pred = clf.predict(Xa_test)
        accA = accuracy_score(y_test, y_pred)
        accuracy_listA.append(accA)
        print("Accuracy For Features A where max_dept =", x, " : ", accA,)

    depth = np.arange(len(max_depth_list)) + 1
    plt.plot(depth, accuracy_listA, marker=".")
    plt.title("Feature Columns A - Accuracy Results Where Max-Depth In Range 1 - 35")
    plt.xlabel("Max-Depth")
    plt.ylabel("Accuracy Score In Decimal [0.70 = 70%]")
    plt.show()

############################### FEATURE COLS B ######################################

    Xb = featureColsB
    # print(Xb)

    Xb_train, Xb_test, y_train, y_test = train_test_split(Xb, y, test_size=0.33)

    for x in max_depth_list:
        clf = tree.DecisionTreeClassifier(max_depth=x, random_state=1)
        clf.fit(Xb_train, y_train)
        y_pred = clf.predict(Xb_test)
        accB = accuracy_score(y_test, y_pred)
        accuracy_listB.append(accB)
        print("Accuracy For Features B where max_dept =", x, " : ", accB,)

    depth = np.arange(len(max_depth_list)) + 1
    plt.plot(depth, accuracy_listB, marker=".")
    plt.title("Feature Columns B - Accuracy Results Where Max-Depth In Range 1 - 35")
    plt.xlabel("Max-Depth")
    plt.ylabel("Accuracy Score In Decimal [0.70 = 70%]")
    plt.show()

############################### FEATURE COLS C ######################################

    Xc = featureColsC
    # print(Xc)

    Xc_train, Xc_test, y_train, y_test = train_test_split(Xc, y, test_size=0.33)

    for x in max_depth_list:
        clf = tree.DecisionTreeClassifier(max_depth=x, random_state=1)
        clf.fit(Xc_train, y_train)
        y_pred = clf.predict(Xc_test)
        accC = accuracy_score(y_test, y_pred)
        accuracy_listC.append(accC)
        print("Accuracy For Features C where max_dept =", x, " : ", accC,)

    depth = np.arange(len(max_depth_list)) + 1
    plt.plot(depth, accuracy_listC, marker=".")
    plt.title("Feature Columns C - Accuracy Results Where Max-Depth In Range 1 - 35")
    plt.xlabel("Max-Depth")
    plt.ylabel("Accuracy Score In Decimal [0.70 = 70%]")
    plt.show()

############################### FEATURE COLS D ######################################

    Xd = featureColsD
    # print(Xd)

    Xd_train, Xd_test, y_train, y_test = train_test_split(Xd, y, test_size=0.33)

    for x in max_depth_list:
        clf = tree.DecisionTreeClassifier(max_depth=x, random_state=1)
        clf.fit(Xd_train, y_train)
        y_pred = clf.predict(Xd_test)
        accD = accuracy_score(y_test, y_pred)
        accuracy_listD.append(accD)
        print("Accuracy For Features D where max_dept =", x, " : ", accD,)

    depth = np.arange(len(max_depth_list)) + 1  # Create domain for plot
    plt.plot(depth, accuracy_listB, marker=".")
    plt.title("Feature Columns D - Accuracy Results Where Max-Depth In Range 1 - 35")
    plt.xlabel("Max-Depth")
    plt.ylabel("Accuracy Score In Decimal [0.70 = 70%]")
    plt.show()

    # print(accA)
    # print(accB)
    # print(accC)
    # print(accD)

    """
    (A) Dataset A (featureColsA) has the best accuracy out of the 4 datasets.
    
    (B) Rainfall appears to be the most important role in predicting RainTomorrow. We can see that 
        the all datasets that have the attribute Rainfall appear to be more accurate. 
        FeatureCols A, C and D are the most accurate of the 4 and all contain Rainfall.
        
    (C) Based on the graphs, the models are most accurate with a lower max_depth. The optimal value appears to be 
        between 4 and 6.  The max_depth corresponds to the path depth of the decision tree and depending on the 
        number of attributes in the feature columns, determines which depth is optimal for that model.
    """


def Task2():

    df['Pressure'] = df[['Pressure9am', 'Pressure3pm']].mean(axis=1)
    # print(df['Pressure'])

    df['Humidity'] = df[['Humidity9am', 'Humidity3pm']].mean(axis=1)
    # print(df['Humidity'])

    subDF = df[['Pressure', 'Humidity', 'RainToday']]
    # print(subDF.shape)

    df_clean = subDF.dropna()
    # print(df_clean.shape)

    X = df_clean[['Pressure', 'Humidity']]
    y = df_clean['RainToday']

    #models = [('KNC', KNeighborsClassifier()), ('DTC', tree.DecisionTreeClassifier()), ('GNB', GaussianNB()),
    #          ('RFC', RandomForestClassifier()), ('SVC', SVC())]

    models = [('KNC', KNeighborsClassifier()), ('DTC', tree.DecisionTreeClassifier()), ('GNB', GaussianNB())]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    results_train = []
    results_test = []
    names = []
    accuracy = 'accuracy'
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10)

        # Train Accuracy
        mod_results_train = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=accuracy)
        results_train.append(mod_results_train)
        # Test Accuracy
        mod_results_test = model_selection.cross_val_score(model, X_test, y_test, cv=kfold, scoring=accuracy)
        results_test.append(mod_results_test)
        # Append names
        names.append(name)

        print(f"|Train Accuracy| Model: {name}, Accuracy: {mod_results_train.mean()}")
        print(f"|Test Accuracy| Model: {name}, Accuracy: {mod_results_test.mean()}")

    # print(len(results_train))
    # print(len(results_test))

    x = np.arange(len(names))
    width = 0.40

    plt.bar(x-0.2, results_test, width)
    plt.bar(x+0.2, results_train, width)
    plt.show()



#def Task3():
#def Task4():


#Task1()
Task2()




