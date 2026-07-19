import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
y = x ** 2

plt.plot(x, y, color="blue", linewidth=2)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
