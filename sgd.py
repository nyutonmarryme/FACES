import numpy as np
import matplotlib.pyplot as plt

def loss(w, x, y):
    M = np.dot(w,x)*y
    return 2/ (1+np.exp(M))

def df(w, x, y):
    M = np.dot(w, x)*y
    return -2 * (1+np.exp(M)**(-2)*np.exp(M)*x*y)

x_train = [[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]]
x_train = [x + [1] for x in x_train]
x_train = np.array(x_train)
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])