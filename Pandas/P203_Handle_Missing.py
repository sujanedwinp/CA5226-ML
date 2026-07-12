import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

# Artificially introduce missing values
df.iloc[0, 0] = np.nan
df.iloc[5, 2] = np.nan

print("Missing values before:\n", df.isnull().sum())

# Replace missing values with the mean of each column
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nMissing values after:\n", df.isnull().sum())
