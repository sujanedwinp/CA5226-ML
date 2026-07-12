import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

v = np.vstack((a, b))
h = np.hstack((a, b))

print("Array A:\n", a)
print("Array B:\n", b)
print("Vertical Stack:\n", v)
print("Horizontal Stack:\n", h)
