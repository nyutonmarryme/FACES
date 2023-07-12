import numpy as np
import matplotlib.pyplot as plt

def loss(w, x, y):
    M = np.dot(w,x)*y
    return 2/ (1+np.exp(M))

def df(w, x, y):
    M = np.dot(w, x)*y
    return -2 * (1+np.exp(M)**(-2)*np.exp(M)*x*y)

