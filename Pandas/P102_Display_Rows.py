import pandas as pd

df = pd.DataFrame({
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
    "age":         [25, 30, 22, 35, 28, 40, 19],
    "column_name": [5, 15, 8, 20, 12, 7, 18],
    "category":    ["A", "B", "A", "C", "B", "C", "A"]
})

print("First 5 rows:")
print(df.head(5))
