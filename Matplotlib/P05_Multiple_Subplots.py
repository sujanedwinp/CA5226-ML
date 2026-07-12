import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Subplot 1: y = sin(x)
ax1.plot(x, np.sin(x), color="steelblue")
ax1.set_title("y = sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# Subplot 2: random scatter
np.random.seed(7)
ax2.scatter(np.random.rand(50), np.random.rand(50), color="tomato", alpha=0.7)
ax2.set_title("Random Scatter")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

plt.tight_layout()
plt.show()
