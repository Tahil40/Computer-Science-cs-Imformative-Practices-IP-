# Importing Module....
import pandas as pd

"""
Series is Type of Dataframe in pandas Library
"""

# Creating Scalar series passing index is must important....
series_scalar = pd.Series(20, index=[1, 2, 3, 4, 5])
print(series_scalar)

series_scalar0 = pd.Series("Harry", index=[1, 2, 3])
print(series_scalar0)

# Creating Series as List passing integer Datatype....
series = pd.Series([10, 20, 30, 40, 50])

# Passing Index from 0.....
series_index = pd.Series([100, 200, 300, 400, 500], index=[0, 1, 2, 3, 4])

# Index will be starting from 1.....
series_index0 = pd.Series([5, 10, 15, 20, 25], index=[1, 2, 3, 4, 5])

print(series)
print(series_index)
print(series_index0)

# Creating series as List passing string Datatype.....
series1 = pd.Series(["Harry", "Larry", "Carry", "Narry"])

# Setting Index......
series1_index = pd.Series(["Harry", "Larry", "Carry", "Narry"], index=[1, 2, 3, 4])

series1_index0 = pd.Series(["A", "B", "C", "D", "E"], index=[1, 2, 3, 4, 5])

print(series1)
print(series1_index)
print(series1_index0)

# Creating Series from Range Function....
series_range = pd.Series(range(0, 20))
# Creating Difference of 2 between series....
series_range0 = pd.Series(range(0, 20, 2))

series_range1 = pd.Series(range(0, 5), index=[1, 2, 3, 4, 5])

print(series_range)
print(series_range0)
print(series_range1)

# Creating series as Dictionary Datatype....
series_dictionary = pd.Series({1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",
                               6:"Saturday", 7:"Sunday"})

series_dictionary0 = pd.Series({"Name":"Moosa Khan", "Class":"+2(Commerce)", "Roll_No":"20",
                                "Email":"Moosa@Gmail.com"})
print(series_dictionary)
print(series_dictionary0)
