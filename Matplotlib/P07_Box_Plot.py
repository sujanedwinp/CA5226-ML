import matplotlib.pyplot as plt
import numpy as np

np.random.seed(3)
data = [np.random.normal(loc, 1.0, 50) for loc in [10, 20, 15, 25]]

plt.boxplot(data, labels=["Group A", "Group B", "Group C", "Group D"],
            patch_artist=True,
            boxprops=dict(facecolor="steelblue", alpha=0.6))
plt.title("Box Plot — Dataset Distribution")
plt.ylabel("Value")
plt.show()
