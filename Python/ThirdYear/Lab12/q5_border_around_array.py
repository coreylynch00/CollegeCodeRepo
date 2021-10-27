# Lab 12 Q5
import numpy as np

x = np.ones((3, 3))
print("Original Array: \n", x)

y = np.pad(x, pad_width=2, mode="constant", constant_values=0)
print("\nNew Array: \n", y)
