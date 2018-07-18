# Pie Chart In Python

# References: Python Data Visualization Cookbook
# https://pythonspot.com/en/matplotlib-pie-chart/
# https://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct

import matplotlib.pyplot as plt

# Square figure and axes:

plt.figure(figsize=plt.figaspect(1))

ax = plt.axes([0.1, 0.1, 0.8, 0.8])

# Labels:

food_labels = "Pasta", "Pizza", "Sushi", "Steak"

# Colours:

colours = ['lightblue', 'yellow', 'orange', 'lightgreen']

# Counts

x = [15, 12, 13, 20]

plt.pie(x, labels = food_labels, autopct='%1.1f%%', colors = colours, startangle=67, 
     shadow = True)

plt.title("Favourite Foods Survey \n")

plt.show()

# Display percentage and number for each piece in the pie chart.

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = val=int((pct*total/100.0)+0.5)
        return '{p:.2f}%  [{v:d}]'.format(p=pct,v=val)
    return my_autopct

plt.pie(x, labels = food_labels, autopct=make_autopct(x), colors = colours, 
        startangle=67, shadow = True)

plt.title("Favourite Foods Survey \n")

plt.show()



