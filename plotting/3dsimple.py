from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [-10, 3, 4, 5, 10]
Y = [100, 150, 250, 320, 400]
Z = [12, 23, 33, 44, 52]

ax.plot(X,Y,Z, ls="None", marker="o")

ax.set_xlabel("X")


plt.show()
