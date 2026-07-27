
import numpy as np

a2d = np.random.randint(0, 10, (2, 3))
a1d = np.arange(0, 10)

a2d2 = np.random.randint(0, 10, (3, 4))
matmul= np.matmul(a2d, a2d2)

darr = a2d2[0:3, 0:3]
dtmt = np.linalg.det(darr)

print(f"Array 1Dr: {a1d[::-1]}")
print(f"Array 2D:\n{a2d}\n3rd Col: {a2d[:,2]}")
print(f"Above 2D Array *\n{a2d2}\n{matmul}")
print(f"For Array:\n{darr}\nDeterminant: {dtmt}")
