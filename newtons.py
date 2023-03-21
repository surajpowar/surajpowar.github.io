# Author: Suraj Powar
# Date: 03/21/2023
# Newton's Method for Numerical Approximation.

import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return x**3 - x**2 + 2* x + 5

def fprime(x):
    return 3*x**2 - 2*x + 2


def newtons(x):
    h = f(x) / fprime(x)
    while abs(h) >= 0.000001:
        h = f(x)/fprime(x)
        x = x - h
        print(x)
     
    print("The value of the root is : ", "%.4f"% x)
    x_plot = np.linspace(-2, 2, 1000)
    y_plot = f(x_plot)
 

    fig = plt.figure()
    plt.plot(x_plot, y_plot, c="blue")
    plt.plot(f(x), fprime(x), c="red", marker="o", fillstyle="none")
    plt.xlim([-5, 5])
    plt.ylim([-15, 15])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Newton's Method")
    plt.grid()
    plt.show()


 
if __name__ == "__main__":
    x_0 = -20 
    newtons(x_0)
