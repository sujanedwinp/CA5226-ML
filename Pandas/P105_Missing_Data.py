import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":  ["Alice", "Bob", None, "Diana", "Eve"],
    "age":   [25, np.nan, 22, 35, np.nan],
    "score": [88, 75, np.nan, 60, 85]
})

print("Count:\n", df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())
df = df.dropna()
print("\nNew DataFrame:\n", df)
