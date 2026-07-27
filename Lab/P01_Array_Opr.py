import pandas as pd
import numpy as np

array_1d = np.arange(0, 10)
array_2d = np.random.randint(0, 10, size=(3, 4))

mean = array_1d.mean()
stddev = array_1d.std()
normalize = ((array_1d - mean)/stddev)

print(f"1D:\n{array_1d}\n2D:{array_2d}")
print(f"Array_1D:\nMean: {mean}\nStdDev: {stddev}\nNrmlzd: {normalize}")
