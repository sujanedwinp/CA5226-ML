import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

cvs = np.array([2, 3, 4])

result = arr * cvs[:, np.newaxis]

print("Original:\n", arr)
print("Constants:", cvs)
print("Result:\n", result)
