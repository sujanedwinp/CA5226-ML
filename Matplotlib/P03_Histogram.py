import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(500)

plt.hist(data, bins=20, color="blue", edgecolor="white")
plt.title("Histogram (20 bins)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
