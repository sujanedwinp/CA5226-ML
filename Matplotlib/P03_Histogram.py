import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.randn(500)   # 500 normally distributed values

plt.hist(data, bins=20, color="mediumpurple", edgecolor="white")
plt.title("Histogram (20 bins)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
