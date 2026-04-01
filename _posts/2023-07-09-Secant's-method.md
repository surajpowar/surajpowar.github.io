---
title:  "Secant Method for Approximation"
mathjax: true
layout: post
categories: media
---

# Secant Method for Numerical Approximation.
If we recall from the [Newton's Method](https://surajpowar.github.io/Newton's-method), the root was determined by the first order Taylor's Series expansion.

$$F(x) = f(x_0) + f'(x_0) (x - x_0)$$

We can determine the root by determining the linear function which corresponds to a line that connects two points on the graph of the function $$f(x)$$.

We know that if a line passing through two points say $$(a_0, b_0)$$ and $$(a_1, b_1)$$, the equation of that line is given by, 

$$y = b_0 + \frac{b_{1} - b_{0}}{a_{1} - a_{0}} (x - a_{0})$$

So, let us consider $$(a_0, f(a_0))$$ and $$(a_1, f(a_1))$$, be two points on the graph of $$f(x)$$

$$y = F(x) $$
$$y = f(a_0) + \frac{a_{1} - a_{0}}{a_{1} - a_{0}} (x - a_{0})$$

Now the function $f(x)$ has a zero value at $$a_2$$ then,

$$0 = f(a_0) + \frac{a_{1} - a_{0}}{a_{1} - a_{0}} (a_2 - a_{0})$$

$$a_2 = a_0 - f(a_0) \frac{a_1 - a_0}{f(a_1) - f(a_0)} $$

We can also interpret the above equation for more iteration in the form of,

$$a_{n+1} = a_n -  f(a_n) \frac{a_n - a_{n - 1}}{f(a_n) - f(a_{n - 1})} $$

The advantage of secant method is the rate of convergence is faster relative to the bisection method.

This method utilizes two recent approximations of the root to compute a new approximation, rather than using only the approximation that is bounded by the interval to enclose the respective root. The only setback of Secant method is we can always have a convergence.





# Code
```python3

# Secant Method for Numerical Approximation
# Date: 07/7/2023

import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import *
from math import *

func =  lambda x : x**2 -2

init_guess_1 = 1

init_guess_2 = 2

error = 0.00001

step = 1

condition = True

while condition:
    if func(init_guess_1) == func(init_guess_2):
        print("Error")
        break
    
    init_guess_3 = init_guess_1 - ((init_guess_2 - init_guess_1)*func(init_guess_1))/ (func(init_guess_2 - func(init_guess_1)))
    init_guess_1 = init_guess_2
    init_guess_2 = init_guess_3
    step = step + 1

    if step > 1000:
        print("Not convergent")
        break

    condition = abs(func(init_guess_3)) > error

print(init_guess_3)


xvals = np.linspace(-2, 6, num=100)
yvals = func(xvals)
plt.plot(xvals,yvals, label = "y = x^2 - 2")
plt.plot(float(init_guess_3), float(func(init_guess_3)), "o", label = float(init_guess_3))
plt.title("Secant Method for Numerical Approximation")
plt.legend()
plt.show()

```

# Ouput
![Figure1](/assets/Figure_3.png)

Thank you for reading.
