import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 8)
means = [np.random.normal(i*2, 1, 20).mean() for i in x]
stds  = [np.random.normal(i*2, 1, 20).std() for i in x]

plt.errorbar(x, means, yerr=stds, fmt="-o", color="blue",
             ecolor="red", elinewidth=2, capsize=5, label="Mean ± Std")
plt.title("Line Plot with Error Bars")
plt.xlabel("Data Point")
plt.ylabel("Value")
plt.legend()
plt.show()
