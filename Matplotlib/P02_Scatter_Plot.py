import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
X1, Y1 = np.random.rand(30), np.random.rand(30)
X2, Y2 = np.random.rand(30) + 0.5, np.random.rand(30) + 0.5

plt.scatter(X1, Y1, color="tomato",    label="Set 1", alpha=0.8)
plt.scatter(X2, Y2, color="steelblue", label="Set 2", alpha=0.8)
plt.title("Scatter Plot — Two Sets of Random Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
