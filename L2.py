import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10.1, 0.1)
y = np.array([a**3 - 10*a**2 + 3*a +500 for a in x])
x_train, y_train = x[::2], y[::2]
N = 13
L = 0