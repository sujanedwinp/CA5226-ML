import pandas as pd

df = pd.DataFrame({
    "name":     ["Alice", "Bob", "Charlie"],
    "score":    [88, 75, 92],
    "category": ["A", "B", "A"]
})

df["grade"] = df["score"].apply(lambda x: "Pass" if x >= 80 else "Fail")

df.to_csv("output_data.csv", index=False)
print("\nOutput CSV:")
with open("output_data.csv", "r") as file:
    print(file.read())
