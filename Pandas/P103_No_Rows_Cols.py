import pandas as pd

df = pd.DataFrame({
    "name":     ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":      [25, 30, 22, 35, 28],
    "score":    [88, 75, 92, 60, 85],
    "category": ["A", "B", "A", "C", "B"]
})

rows, cols = df.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
