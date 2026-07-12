import numpy as np

nums = np.arange(10)

nnums = nums.reshape(2, 5)

print("1D Array:", nums)
print("Reshaped (2x5):\n", nnums)
