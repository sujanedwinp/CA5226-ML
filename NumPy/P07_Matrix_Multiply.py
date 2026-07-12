import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7,  8,  9,  10],
              [11, 12, 13, 14],
              [15, 16, 17, 18]])

r = np.matmul(A, B)

print("A:\n", A)
print("B:\n", B)
print("A * B:\n", r)
