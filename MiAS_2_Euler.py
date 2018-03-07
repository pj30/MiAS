import numpy as np
import matplotlib.pyplot as mtpl
import pylab

h = 0.1 # time step
a = 2
T = 6
t = np.arange(0, T, h)
N = t.size # liczba kroków symulacji
X = np.zeros(N)
X[0] = 0.1 # warunek początkowy
for i in range(1, N):
    #X[i] = X[i - 1] + (h * a * X[i - 1] * (1 - X[i - 1]))
    X[i] = X[i - 1] + (h * t[i - 1] * X[i - 1])

mtpl.plot(X)
mtpl.plot(X, 'go')
pylab.show()
