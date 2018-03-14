import numpy as np
import matplotlib.pyplot as mtpl
import pylab

h = 0.01 # time step
a = 0
b = 1
T = 50
t = np.arange(0, T, h)
N = t.size # liczba kroków symulacji
X = np.zeros(N)
Y = np.zeros(N)
X[0] = 10 # warunek początkowy
Y[0] = -2
for i in range(1, N):
    dX = 0.5 * X[i - 1] - Y[i - 1] - 0.5*(X[i - 1] ** 3 + X[i - 1] * (Y[i - 1]**2))
    X[i] = X[i - 1] + h * dX
    dY = X[i - 1] + 0.5 * Y[i - 1] - 0.5*(Y[i - 1]**3 + (X[i - 1]**2) * Y[i - 1])
    Y[i] = Y[i - 1] + h * dY

mtpl.plot(t, X, 'k', label = 'X')
mtpl.plot(t, Y, 'g', label = 'Y')
mtpl.legend(loc = 'upper right', fontsize = '14')
mtpl.xlabel("t")
mtpl.ylabel("stan")
pylab.show()
