#import matplotlib libary
import matplotlib.pyplot as plt


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 120.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#show plot
plt.show()
