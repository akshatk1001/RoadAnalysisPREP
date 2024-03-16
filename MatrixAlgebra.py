import pandas as pd
import numpy as np

a1 = np.array([2, 1, -3, -4])
b1 = np.array([4, -2, 1, 9])
c1 = np.array([3, 5, -2, 5])

def findLCM(a, b):
    lcm = 0
    if (a > b):
        lcm = a
    else:
        lcm = b
    while True:
        if (lcm % a == 0 and lcm % b == 0):
            break
        lcm += 1
    return lcm

def solveMatrix(a, b, c):
    lcm1 = findLCM(a[0], b[0])
    b = (b * (lcm1/b[0])) - (a * (lcm1/a[0]))
    lcm2 = findLCM(a[0], c[0])
    c = (c * (lcm2/c[0])) - (a * (lcm2/a[0]))
    lcm3 = findLCM(b[1], c[1])
    c = (c * (lcm3/c[1])) - (b * (lcm3/b[1]))

    z_val = c[3]/c[2]
    print("z = ", z_val, "\n")

    y_val = (b[3] - (b[2] * z_val))/b[1]
    print("y = ", y_val, "\n")

    x_val = (a[3] - (a[1] * y_val) - (a[2] * z_val))/a[0]
    print("x = ", x_val, "\n")


solveMatrix(a1, b1, c1)
