import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


data = np.genfromtxt("curve-data.csv", delimiter=",")

xdata = data[:,0]
ydata = data[:,1]

plt.scatter(xdata,ydata)

def f(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
fit = curve_fit(f,xdata,ydata)

a = fit[0][0]
b = fit[0][1]
c = fit[0][2]
d = fit[0][3]

plt.plot(xdata,f(xdata,a,b,c,d))

plt.title("x against y")
plt.xlabel("x datafrom file")
plt.ylabel("y data from file")

plt.show()


