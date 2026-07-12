import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.plot(x, y, color="seagreen", linewidth=2, linestyle="--", label="cos(x)")
plt.title("Customized Plot — y = cos(x)", fontsize=14, fontweight="bold")
plt.xlabel("x-axis", fontsize=12)
plt.ylabel("y-axis", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle=":", alpha=0.7)
plt.show()
