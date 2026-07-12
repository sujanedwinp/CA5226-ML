import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x = np.arange(1, 8)

# Simulate mean and std from samples at each point
means = np.array([np.random.normal(i * 2, 0.5, 20).mean() for i in x])
stds  = np.array([np.random.normal(i * 2, 0.5, 20).std()  for i in x])

plt.errorbar(x, means, yerr=stds, fmt="-o", color="steelblue",
             ecolor="tomato", elinewidth=2, capsize=5, label="Mean ± Std")
plt.title("Line Plot with Error Bars")
plt.xlabel("Data Point")
plt.ylabel("Value")
plt.legend()
plt.grid(True, alpha=0.4)
plt.show()
