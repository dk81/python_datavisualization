# Bar Graphs In Python

# References: Python Data Visualization Cookbook
# https://pythonspot.com/en/matplotlib-bar-chart/
# https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
# https://stackoverflow.com/questions/21321670/how-to-change-fonts-in-matplotlib-python
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

colours = ("Red", "Green", "Blue", "Black", "Orange", "Purple")
y_position = np.arange(len(colours))

y = [8, 11, 14, 10, 12, 20]


# Bar Graph:

plt.bar(y_position, y, width = 0.5, align = "center", color = "lightgreen",
        label = "Class #1")
        
# Labels And Title:

plt.xlabel("Colour")
plt.xticks(y_position, colours)
plt.ylabel("Count")
plt.title("Favourite Colour Survey Results \n")
plt.legend(loc = "upper right")

axes = plt.gca()
axes.set_ylim([0, 25])

plt.show()




#--------------------------------
## Horizontal Bar Graph:

# Bar Graph:

plt.barh(y_position, y, align = "center", color = "lightblue",
        label = "Class #1")

# Labels And Title:

plt.ylabel("Colour \n")
plt.yticks(y_position, colours)
plt.xlabel("\n Count")

csfont = {'fontname':'Comic Sans MS'}

plt.title("Favourite Colour Survey Results \n ", **csfont)
plt.legend(loc = "bottom right")

axes = plt.gca()
axes.set_xlim([0, 25])


plt.show()

#--------------------------------

# Side By Side Bar Graphs:

import numpy as np
import matplotlib.pyplot as plt

colours = ("Red", "Green", "Blue", "Black", "Orange", "Purple")

class_one = [8, 11, 14, 10, 12, 20]

class_two = [5, 12, 10, 17, 8, 12]

# Bar Graph:

fig, ax = plt.subplots()
y_position = np.arange(len(colours))
bar_width = 0.4

bar1 = plt.bar(y_position, class_one, bar_width , color = "lightgreen",
        label = "Class #1")
        
bar2 = plt.bar(y_position + bar_width, class_two, bar_width , color = "red",
        label = "Class #2")
        
# Labels And Title:

plt.xlabel("\n Colour")
plt.ylabel("Count \n")

csfont = {'fontname':'Comic Sans MS'}
plt.title("Favourite Colour Survey Results \n", **csfont)

plt.xticks(y_position + bar_width, colours)
plt.legend(loc = "upper left")

axes = plt.gca()
axes.set_ylim([0, 25])


plt.show()

#----------------------------------------

## Sorted Horizontal Bar Graph (Updated part on May 9, 2018):
# References: https://stackoverflow.com/questions/28022227/sorted-bar-charts-with-pandas-matplotlib-or-seaborn
# https://stackoverflow.com/questions/21487329/add-x-and-y-labels-to-a-pandas-plot
# https://stackoverflow.com/questions/20600006/simple-customization-of-matplotlib-pandas-bar-chart-labels-ticks-etc

colours = ("Red", "Green", "Blue", "Black", "Orange", "Purple", "Pink", "Yellow")
y_position = np.arange(len(colours))

y = [5, 7, 9, 6, 3, 4, 10, 5]

# Create pandas dataframe:

sample_data = pd.DataFrame({"Colour": colours, "Count": y})

# Sort by Counts:

sorted = sample_data.sort_values(by = "Count", ascending = False)

# Font

csfont = {'fontname':'Comic Sans MS'}

# Graph Part

fig, ax = plt.subplots()

ax.barh(y_position, sorted["Count"] , align='center',
        color= '#99CC66', ecolor='black')
        
# Aesthetics:

ax.set_yticks(y_position)
ax.set_yticklabels(colours, **csfont)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('\n Count', **csfont)
ax.set_ylabel('Favourite Colour \n', **csfont)
ax.set_title('Student Survey Of Favourite Colours \n', **csfont)
ax.set_xlim([0, 12])

# Text Labels On Bar:

for i, v in enumerate(sorted["Count"]):
    ax.text(v + 0.1, i + .15, str(v), color = '#3333FF', fontweight='bold')

plt.show()












