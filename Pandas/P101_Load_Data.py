import pandas as pd

test = pd.DataFrame({
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":         [25, 30, 22, 35, 28],
    "column_name": [5, 15, 8, 20, 12],
    "category":    ["A", "B", "A", "C", "B"],
    "date":        ["2024-01-15", "2024-03-22", "2024-06-05", "2024-09-10", "2024-11-30"]
})
test.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")
print("DataFrame loaded from data.csv:")
print(df)
