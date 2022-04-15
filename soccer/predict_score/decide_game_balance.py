import random
import numpy as np
import numpy.random as rd
import statistics

x = np.array([-99, -95, -90,-80, -50, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([0.03, 0.04, 0.05, 0.06, 0.07, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
r = -98
coe = np.polyfit(x,y,2)
Y = coe[0] * r ** 2 + coe[1] * r + coe[2]
print(Y)
print(coe)

for r in range(-1,-100):
    if coe[0] * r ** 2 + coe[1] * r + coe[2] < 0:
        print(r,)