import pandas as pd

df = pd.DataFrame({
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "column_name": [5, 15, 8, 20, 12],
    "category":    ["A", "B", "A", "C", "B"]
})

df_filtered = df[df["column_name"] > 10]
print("Original DataFrame:\n", df)
print("\nFiltered (column_name > 10):\n", df_filtered)
