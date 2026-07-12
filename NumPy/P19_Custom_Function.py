import numpy as np


def power(x):
    return x ** 2

v = np.vectorize(power)

nums = np.array([0, 1, 2, 3, 4, 5])
r = v(nums)

print("Input:", nums)
print("f(x) = x^2 ->\n", r)
