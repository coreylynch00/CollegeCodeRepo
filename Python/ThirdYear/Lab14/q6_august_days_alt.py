# Lab 14 Q6 Alternate

import numpy as np

aug = np.arange('2019-08', '2019-09', dtype='datetime64[D]')

# aug[start : stop : skip]
evenDays = aug[1:31:2]

for i in evenDays:
    print(i)
