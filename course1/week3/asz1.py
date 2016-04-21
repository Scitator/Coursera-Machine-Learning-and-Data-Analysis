import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
	return np.sin(x / 5.0) * np.exp(x / 10.0) + 5.0 * np.exp(-x / 2.0)


x_min =  optimize.minimize(f, 2.0,method='BFGS')
print f(x_min.x)
x_min = optimize.minimize(f, 30.0,method='BFGS')
print f(x_min.x)
x_min =  optimize.differential_evolution(f, [(1.0, 30.0)])
print f(x_min.x)

print ""
def h(x):
	return int(f(x))

x_min = optimize.minimize(h, 30,method='BFGS')
print h(x_min.x)
x_min =  optimize.differential_evolution(h, [(1, 30)])
print h(x_min.x)

#x = np.arange(1, 30, 0.1)
#y = h(x)
#plt.plot(x, y, '-')
#plt.show()