import pandas as pd

data = [[1, "Chris", 10], [20, "John", 11], [13, "Tysen", 12], [14, "Rock", 9]]

data_frames = pd.DataFrame(data, index=["R1", "R2", "R3", "R4"],
                                columns=["Roll_No", "Name", "Class"])

print(data_frames)
print(data_frames.at["R1", "Name"]) # To Get The name of R1....
data_frames.iat[1,2] = 12 # Change the value at Given Index....
print(data_frames.iat[1,2]) # Get Indexing value of The DataFrame....
print(data_frames.iloc[1,0:2]) # Slicing the Dataframe....
print(data_frames.loc["R2", "Name":"Class"]) # Name and Class must be Return....
print(data_frames.loc["R3":"R2":-1]) # Reversing The Rows in DataFrames.....
