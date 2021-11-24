from matplotlib import pyplot as plt
import random
import numpy as np
def y(x):
    return x**2
def dy(x):
    return 2*x
xs = np.linspace(-5,5,100) 
ys = xs**2
plt.plot(xs,ys, 'g')
x = [5]
a = 0.9
y=[x[0]**2]
for i in range(1000):
    x.append(x[-1]-a*dy(x[-1]))
    y.append(x[-1]**2)
    if -1e-6<x[-1]<1e-6:
        print(i)
        break
plt.scatter(x,y)
# print(x)
# print(y)
plt.axis([-10,10,-1,30])
plt.show()
