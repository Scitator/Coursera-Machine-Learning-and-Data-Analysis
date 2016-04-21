import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import linalg

def f(x):
	return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
def g(w0, w1, w2, w3, x):
	return w0

a = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([f(1.0), f(4.0), f(10.0), f(15.0)])
x = linalg.solve(a, b)
print x

x_test = np.arange(1, 15, 0.1)
y = x[0] + x[1] * x_test + x[2] * x_test**2 + x[3] * x_test**3
ynew = f(x_test)
plt.plot(x_test, y, '-', x_test, ynew, 'o')
plt.show()