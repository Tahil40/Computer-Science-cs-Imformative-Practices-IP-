# importing Module....
import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 30] # set the x-axis....
y = [100, 200, 300, 400, 250] # set the y-axis....
plt.ylim(300, 450) # set The limit of y-axis...
plt.xlim(15, 30) # set the limit of x-axis....
plt.plot(x, y, color='blue') # Passing axes and set colour...
plt.grid(True) # Used to show grid in Graph....
plt.title("Sales Report") # used to set the tittle of Graph...
plt.xlabel("Years") # set the x-axes...
plt.ylabel("Profit") # set the y-axes...

# if you want to make it bar graph....
plt.bar(x, y, color=['blue', 'red'])
plt.grid(True)

plt.show()
