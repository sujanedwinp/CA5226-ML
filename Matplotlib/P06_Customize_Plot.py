import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D", "E"])
y = np.array([5, 7, 3, 8, 6])

plt.plot(x, y, color="blue", linewidth=2, label="cos(x)")
plt.title("Customized Plot", fontsize=14, fontweight="bold")
plt.xlabel("Name", fontsize=12)
plt.ylabel("Points", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True)
plt.show()
