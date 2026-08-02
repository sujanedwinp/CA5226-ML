import pandas as pd

data = [23, 34, 65, 87, 32, 78, 43]

s = pd.Series(data)

print("Mean:", s.mean())
print("Median:", s.median())
print("Mode:")
print(s.mode())
print("Variance:", s.var())
print("Standard Deviation:", s.std())
print(data.describe())