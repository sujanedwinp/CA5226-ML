import matplotlib.pyplot as plt
import numpy as np

X1, Y1 = np.random.rand(30), np.random.rand(30)
X2, Y2 = np.random.rand(30), np.random.rand(30)

plt.scatter(X1, Y1, color="red", label="Set 1")
plt.scatter(X2, Y2, color="blue", label="Set 2")
plt.title("2 Random Scatter Plots")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
