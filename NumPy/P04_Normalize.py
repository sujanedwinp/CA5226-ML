import numpy as np

# Normalize: (subtract the mean and divide by std deviation)z
nums = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

normalized = (nums - np.mean(nums)) / np.std(nums)

print("Original:", nums)
print("Normalized:", normalized)
