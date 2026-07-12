import pandas as pd

df1 = pd.DataFrame({
    "id":   [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"]
})

df2 = pd.DataFrame({
    "id":    [2, 3, 4, 5],
    "score": [85, 90, 78, 92]
})

merged = pd.merge(df1, df2, on="id")
print("DF1:\n", df1)
print("\nDF2:\n", df2)
print("\nMerged DF:\n", merged)
