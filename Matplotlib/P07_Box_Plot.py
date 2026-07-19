import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(10, 1, 50),
        np.random.normal(20, 1, 50),
        np.random.normal(15, 1, 50),
        np.random.normal(25, 1, 50)]

plt.boxplot(data)
plt.title("Distribution Box Plot")
plt.ylabel("Value")
plt.show()
