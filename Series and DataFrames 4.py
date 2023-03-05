# Importing Modules....
import pandas as pd

# Creating data and passing as List Datatypes......
data = [[1, "Harry", "+1(Medical)", "Harry@Gmail.com"],
        [2, "Larry", "+1(Non-Medical)", "Larry@Gmail.com"],
        [3, "Carry", "+1(Arts)", "Carry@Gmail.com"],
        [4, "Marry", "+1(Commerce)", "Marry@Gmail.com"]]

# Creating dataframes....
data_frames = pd.DataFrame(data,columns=["Roll_No", "Name", "Class", "Email"])
data_frames.index = ["R1", "R2", "R3", "R4"]
print(data_frames)

# Creating data and passing dictionary as Datatypes....
data_Dictionary = [{"Roll_No": 1, "Name": "Harry1", "Class": "+2(N.Medical)", "Email": "Harry1@Gmail.com"},
                   {"Roll_No": 2, "Name": "Larry1", "Class": "+2(Medical)", "Email": "Larry1@Gamil.com"},
                   {"Roll_No": 3, "Name": "Carry1", "Class": "+2(Arts)", "Email": "Carr1@Gmail.com"},
                   {"Roll_No": 4, "Name": "Marry1", "Class": "+2(Commerce)", "Email":"Marry1@Gmail.com"}]
data_frames_Dictionaries = pd.DataFrame(data_Dictionary)
data_frames_Dictionaries.index = ["R1", "R2", "R3", "R4"]
print(data_frames_Dictionaries)

data_Dictionary0 = {"Roll_No": [1, 2, 3, 4],
                    "Name": ["Harry2", "Larry2", "Carry2", "Marry2"],
                    "Class": ["+2(N.Medical)", "+2(Medical)", "+2(Arts)", "+2(Commerce)"],
                    "Email": ["Harry2@Gmail.com", "Larry2@Gmail.com", "Carry2@Gmail.com", "Marry2@Gmail.com"]}

data_frames_Dictionaries0 = pd.DataFrame(data_Dictionary0)
data_frames_Dictionaries0.index = ["R1", "R2", "R3", "R4"]
print(data_frames_Dictionaries0)
print(data_frames_Dictionaries0.T) # Used to Transpose the Column and Row in a DataFrames.....

s1 = pd.Series([1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])
s2 = pd.Series([6, 7, 8, 9, 10], index=["A", "B", "C", "D", "E"])

print(pd.DataFrame([s1, s2]))
