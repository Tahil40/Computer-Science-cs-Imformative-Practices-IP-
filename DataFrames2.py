import pandas as pd

data = {
        "Roll_No": [1, 2, 3, 4],
       "Name": ["Harry", "Larry", "Carry", "Narry"],
       "Class": ["10", "10", "9", "9"],
       "Email": ["Harry@Gmail.com", "Larry@Gmail.com", "Carry@Gmail.com", "Narry@Gmail.com"]
        }

data_frames = pd.DataFrame(data)
data_frames.index = ["R1", "R2", "R3", "R4"]
print(data_frames.index) # Give the Index of Dataframes......
print(data_frames.values) # Give The Value of Dataframes....
print(data_frames.columns) # Return The Column of Dataframes....
print(data_frames.axes) # Return Both The Axes of Dataframes....
print(data_frames.ndim) # Return The Dimentions of Dataframes....
print(data_frames.shape) # Return The Shape of Dataframes....
print(data_frames.size) # Return The Size of Dataframes...
print(data_frames.empty) # Return true for empty dataframes and return true for elements in dataframe.....
print(data_frames.T) # Transpose the Rows and Columns.....
print(data_frames.head(2)) # return The upper two rows of dataframes....
print(data_frames.tail(2)) # return The lower two rows of Dataframes....
print(data_frames.tail(-3)) # Show the last rows and left first three rows.......

# Solving Methods using dots....
print(data_frames.tail(-2).head(1)) # Operate those condition first that are before dot(.) and then solve the second condition that is after the dot(.).....

print(data_frames.count())
print(data_frames.max())
print(data_frames.min())
print(data_frames.sum())
print(data_frames["Roll_No"].mean()) # Perform operation on roll_no row you can also find average using dot(.) .....
print(data_frames.Roll_No.mean()) # .................
data_frames["Roll_No"] = .60*data_frames.Roll_No # Method used to return 60% of roll_no......
print(data_frames)

# Adding New columns to Dataframes.....
data_frames["Phone Number"] = [9234567891, 9236541025, 921025487, 921021111]
print(data_frames)

# Adding New Rows to Dataframes loc function is used to add new row.......
data_frames.loc["R5"] = [5, "Marry", 10, "Marry@Gmail.com", 36259810]
print(data_frames)

# deleting data from dataframes.....
data_frames = data_frames.drop("R1")
data_frames.drop("R5", inplace=True) # Another Method to Delete.....
data_frames.drop(["R2", "R3"], inplace=True) #.......
print(data_frames)

data_frames.drop("Name", inplace=True, axis=1) # Used to delete column from Dataframe.....
del data_frames["Name"] # ...........
data_frames.pop("Name") # ...........
print(data_frames)
