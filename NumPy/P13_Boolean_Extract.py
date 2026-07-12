import numpy as np

nums = np.random.rand(10)

filtered = nums[nums > 0.5]

print("Random Array:", nums)
print("Elements > 0.5:", filtered)
