from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)

ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

ax.set_zlim3d(0, 80)
plt.show()
