import numpy as np

m = np.array([[1, 2, 5],
              [4, 7, 3],
              [4, 2, 1]])

det = np.linalg.det(m)

print("Matrix:\n", m)
print("Determinant:", det)
