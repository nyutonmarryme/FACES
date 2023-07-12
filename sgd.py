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

n_train = len(x_train)
w = [0.0, 0.0, 0.0]
nt = 0.0005  # шаг сходимости SGD
lm = 0.01  # скорость "забывания" для Q
N = 500  # число итераций SGD

Q = np.mean([loss(w, x, y) for x, y in zip(x_train, y_train)])
Q_plot = [Q]

for i in range(N):
    k = np.random.randint(0, n_train-1)
    ek = loss(w, x_train, y_train[k])
    