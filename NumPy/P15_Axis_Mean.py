import numpy as np

nums = np.random.randint(1, 20, size=(3, 4))

print("2D Array:\n", nums)
print("Mean along axis 0 (column):", np.mean(nums, axis=0))
print("Mean along axis 1 (row):", np.mean(nums, axis=1))
