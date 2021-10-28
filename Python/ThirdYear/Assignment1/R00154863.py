#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on a nice day

@author: Corey Lynch

@ID:  R00154863
"""

import numpy as np

#--------------------------------

"""
Beginning of task one
"""
def LineDetector():

    myImmutableCollection = ()
    with open('CountOfMonteCristo.txt') as file:
        for line in file:
            line = line.rstrip("\n")
            if line.startswith("\'") and line.endswith("\'") or line.startswith('\"') and line.endswith('\"'):
                # print(line)   # Undo comment to see that only lines starting/ending with " or ' are selected.
                return myImmutableCollection
    file.close()                    # this is a collection of lines where each line has the aforementioned conditions.


LineDetector()
"""
End of task one
"""









#--------------------------------








"""
Beginning of task two
"""
string = input("Enter a string: ")


def IntegerDetector(inputString):

    integerList = []    # this is a list that will keep the extracted substrings that can be converted into integer numbers from the input string (inputString)
    for char in inputString.split():
        if char.isdigit():
            integerList.append(int(char))
    print(integerList)


IntegerDetector(string)
"""
End of task two
"""






#--------------------------------







"""
Beginning of task three
"""
def CasualUsersAMPM():
    
    am = 0.0    # this is a variable that keeps the average number of casual users before midday
    pm = 0.0    # this is a variable that keeps the average number of casual users after midday

    data = np.genfromtxt('bikeSharing.csv', delimiter=',')
    subset = data[:, 4]
    # print(subset)
    arr_am = np.where(subset < 12)
    arr_pm = np.where(subset >= 12)

    am = np.average(arr_am)
    pm = np.average(arr_pm)
    
    print("Average of Casual Users before midday is ", am)
    print("Average of Casual Users after midday is ", pm)   # I assume there was a typo here so changed to "User after midday"


CasualUsersAMPM()
"""
End of task three
"""


    
