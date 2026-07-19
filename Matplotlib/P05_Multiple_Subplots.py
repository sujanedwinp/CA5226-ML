import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, np.sin(x))
ax2.scatter(np.random.rand(50), np.random.rand(50))

plt.show()