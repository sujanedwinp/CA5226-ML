import numpy as np

nums = np.random.randint(0, 9, size=(3,2))
print(f"Array:\n{nums}")

print(f"Mean on Rows:\n{np.mean(nums, axis=1)}")
print(f"Mean on Cols:\n{np.mean(nums, axis=0)}")

print(f"Array Multiply\n{nums*[1, 2]}")

nums1d = np.array([45, 23, 54, 95, 67, 89])
print(f"Adding 1 to all:\n{nums1d+1}")
print(f"Min: {np.min(nums1d)}")
print(f"Max: {np.max(nums1d)}")
