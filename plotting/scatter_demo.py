import numpy as np
import pylab as plt

X = np.linspace(0,5,100)
Y1 = X + 2*np.random.random(X.shape)
Y2 = X**2 + np.random.random(X.shape)

plt.scatter(X,Y1,color='k')
plt.scatter(X,Y2,color='g')
plt.show()
