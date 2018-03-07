import numpy as np

def fibbo(length):
    x = np.zeros(length)
    x[0] = 0
    x[1] = 1
    for i in range(2, length):
        x[i] = x[i - 1] + x[i - 2]

    return x

length = int(input("Podaj długość ciągu fibbonaciego: "))
x = fibbo(length)
print(x)
