# Lab 14 Q7

import numpy as np


TNow = np.datetime64('now', 'h')

bd = np.datetime64(input('When is your birthday? '))

print(TNow - bd)
