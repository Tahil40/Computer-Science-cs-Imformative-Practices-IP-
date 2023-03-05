# importing Module....
import matplotlib.pyplot as plt

# for creating multiple bar graph...
x = [5, 10, 15, 20, 30] # set the x-axis....
x0 = [10, 20, 30, 40, 50]
y = [100, 200, 300, 400, 250] # set the y-axis....
y0 = [100, 250, 350, 450, 600]

plt.grid(True) # Used to show grid in Graph....
plt.title("Sales Report") # used to set the tittle of Graph...
plt.xlabel("Years") # set the x-axes...
plt.ylabel("Profit") # set the y-axes...


plt.bar(x, y, color='blue', label="Sales in years") # Passing axes and set colour...
plt.bar(x0, y0, color='red', label="Cost in Rupees")
plt.legend(loc='upper left') # used to show passed label and set the location of label according to user's choice like = upper left, upper right, lower left, lower right....

plt.show()