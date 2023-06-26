---
title:  "Bisection Method for Approximation"
author: Suraj Powar
date: 2023-06-26
mathjax: true
layout: post
categories: media
---

# Bisection Method for Numerical Approximation.
As we are well aware of the fact, that if we have a function say f, the process of root finding is essentially finding a value of x such that, $$ f(x) = 0$$

If the function equals to zero, then we say x is the root of a function. This method is based on the intermediate value theorem or also known as IVT for continuous function. 

\begin{theorem}
Let f be a continuous function on a closed interval [a, b]. Assume that m is a number between f(c) and f(b). Then \\(\exists\\)



\end{theorem}


# Code
```python3
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import *
from math import *

func =  lambda x : x**2 -2
funcprime = lambda x: 2*x 

#initial Guess
x0 = 2
iteration = 20
x1 = x0

guess = []
for i in range(1,iteration):
    x1 = x1 - (func(x1)/funcprime(x1))
    guess = [guess, x1]
    print(guess)

print(x1)
print(np.sqrt(2) - x1)

xvals = np.linspace(-2, 3, num=100)
yvals = func(xvals)
plt.plot(xvals,yvals, label = "y = x^2 - 2")
plt.plot(x1, func(x1), "o", label = x1)
plt.title("Newtons Method for Numerical Approximation")
plt.legend()
plt.show()
```

# Ouput

![](assets/Figure_1.png)
