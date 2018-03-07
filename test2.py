import numpy as np
import matplotlib.pyplot as mtpl
import pylab

h = 0.01 # time step
a = 1
T = 20
t = np.arange(0, T, h)
N = t.size # liczba kroków symulacji
X = np.zeros(N)
X[0] = 0.5 # warunek początkowy
for i in range(1, N):
    X[i] = X[i - 1] + h * (-t[i - 1] * np.sin(a * X[i - 1]))

mtpl.plot(X, 'go')
pylab.show()
