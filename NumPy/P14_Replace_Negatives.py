import numpy as np

nums = np.array([3, -1, 4, -1, 5, -9, 2, 6, -5])
nums[nums < 0] = 0
print("New Array: ", nums)
