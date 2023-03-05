# importing Module....
import numpy as np
import pandas as pd

# Creating series using arrange.....
lst_integer = np.arange(0, 10, 2)
series = pd.Series(lst_integer, index=[1, 2, 3, 4, 5])
print(series)
# Slicing series....
print(series[1:4]) # give elements between 1 and 4....
print(series[::-1]) # Reversing series...

lst_string = np.arange(0, 5)
series0 = pd.Series(lst_string, index=["A", "B", "C", "D", "E"])
print(series0)
print(series0[2:5])
print(series0[::-1])