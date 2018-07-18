# Seaborn Plotting Self-Exercise

# References: 
# https://www.tutorialspoint.com/seaborn/seaborn_quick_guide.htm
# 

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

### Bar Graph Example

fav_subject = ["English", "Math", "Phys. Ed", "French", "Science"]

counts = [8, 4, 7, 5, 8]

fav_subjects = {"Favourite Subject": fav_subject,
                "Count": counts}

subjects_df = pd.DataFrame(fav_subjects)

# Rearrange order in dataframe: 
# https://stackoverflow.com/questions/41968732/set-order-of-columns-in-pandas-dataframe

columnsTitles = ["Favourite Subject", "Count"]

subjects_df  = subjects_df.reindex(columns=columnsTitles)

subjects_df = subjects_df.sort_values(by = 'Count', ascending = False)

print(subjects_df)

# Reference: https://seaborn.pydata.org/generated/seaborn.barplot.html
# Reference: https://stackoverflow.com/questions/31632637/label-axes-on-seaborn-barplot

sns.set_style("whitegrid")

fig  = sns.barplot(x = "Favourite Subject", y = "Count", data= subjects_df)

plt.xlabel("\n Favourite Subject")
plt.ylabel("Counts \n")
plt.title("Favourite School Subject Survey Results\n ", fontsize = 15) 
plt.show(fig)

# Horizontal Bars Graph (Just Switch Order of x and y):
    
sns.set_style("whitegrid")

fig2  = sns.barplot(x = "Count", y = "Favourite Subject", data = subjects_df)

plt.ylabel("Favourite Subject \n")
plt.xlabel("\n Count")
plt.title("Favourite School Subject Survey Results\n ", fontsize = 15) 

plt.show(fig2)


### Histogram Example
# Reference: https://seaborn.pydata.org/tutorial/distributions.html

normals = np.random.standard_normal(10000)

# Darkgrid style (looks like R's ggplot2):
    
sns.set_style("darkgrid")

fig  = sns.distplot(normals, kde = False)

plt.xlabel("\n Number Of Standard Deviations From The Mean")
plt.ylabel("Count \n")
plt.title("Simulated Normal Random Variables (n = 10000) \n") 
plt.show(fig)

### Scatterplot
# Reference: https://python-graph-gallery.com/40-basic-scatterplot-seaborn/

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [-3, 2, -1, 6, 0, 4, 2, 3, -3]

xy_df = pd.DataFrame({"x": x, "y": y})


# Without regression fit:
fig  = sns.regplot(x = xy_df.x, y = xy_df.y, fit_reg=False)

plt.xlabel("\n x")
plt.ylabel("y \n")
plt.title("Basic x vs y Scatterplot \n") 
plt.show(fig)

sns.plt.show()


# With linear regression line:
    
fig  = sns.regplot(x = xy_df.x, y = xy_df.y, fit_reg = True, color = "g")

plt.xlabel("\n x")
plt.ylabel("y \n")
plt.title("Basic x vs y Scatterplot \n With Regression Line \n") 
plt.show(fig)

sns.plt.show()


### Line Graph
    
# Reference: https://python-graph-gallery.com/seaborn/
# https://python-graph-gallery.com/120-line-chart-with-matplotlib/

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [-3, 2, -1, 6, 0, 4, 2, 3, -3]
    
xy_df = pd.DataFrame({"x": x, "y": y})

plt.plot('x', 'y', data= xy_df)

plt.xlabel("\n x")
plt.ylabel("y \n")
plt.title("Basic x vs y Line Graph \n") 

plt.show()

### Math Functions Plot
# Reference: https://glowingpython.blogspot.ca/2011/04/how-to-plot-function-using-matplotlib.html
# https://python-graph-gallery.com/193-annotate-matplotlib-chart/

## Quadratic Parabola Example:
    
x = np.linspace(-20, 20, num = 100)
quadratic_y = x**2

quadratic_df = pd.DataFrame({"x": x, "y": quadratic_y})

sns.set_style("white")
plt.plot('x', 'y', data= quadratic_df)

plt.xlabel("\n x", fontsize = 20)
plt.ylabel("y \n", fontsize = 20)
plt.title("A Basic Quadratic Graph", fontsize = 25) 

#  Math Annotation Text
plt.text(14, 10, r'$y = x^2$', fontsize=20)

plt.show()


## Cubic Function Example:
    
x = np.linspace(-10, 10, num = 100)
cubic_y = x**3

cubic_df = pd.DataFrame({"x": x, "y": cubic_y})


sns.set_style("white")
plt.plot('x', 'y', data= cubic_df)

plt.xlabel("\n x", fontsize = 20)
plt.ylabel("y \n", fontsize = 20)
plt.title("A Cubic Function Example \n", fontsize = 22) 

#  Math Annotation Text
plt.text(-9, 800, r'$y = x^3$', fontsize=25)

plt.show()





