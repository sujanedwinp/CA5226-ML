import pandas as pd

df = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B", "C", "A"],
    "value":    [10, 20, 30, 40, 50, 60, 70]
})

gmean = df.groupby("category")["value"].mean()

print("DataFrame:\n", df)
print("\nMean values in each category:\n", gmean)
