# Histograms In Python:

# References: http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
# Python Data Visualization Cookbook by Igor Milovanovic
# https://docs.scipy.org/doc/numpy-1.12.0/reference/routines.random.html

# Simulation Data:

import numpy as np
import matplotlib.pyplot as plt


# Example One - Standard Uniform Distribution Simulation Results

unifs = np.random.uniform(low = 0, high = 1, size = 10000)

axunif = plt.gca() # gca means get current axes

# Histogram of Simulated Uniforms Data:

axunif.hist(unifs, bins = 30, color = "orange")

axunif.set_xlabel('u')
axunif.set_ylabel('f(u) \n')

axunif.set_title("Standard Uniform Distribution \n Simulation Results (n = 10000) \n")

plt.show()


# Example Two - Standard Normal Distribution Simulation Results

normals = np.random.standard_normal(100000)

axnorm = plt.gca() # gca means get current axes

# Histogram of Simulated Normals Data:

axnorm.hist(normals, bins = 50, color = "green")

axnorm.set_xlabel('z')
axnorm.set_ylabel('f(z)')

axnorm.set_title("Standard Normal Distribution \n Simulation Results (n = 100000) \n")


plt.show()

