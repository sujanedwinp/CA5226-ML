import pandas as pd

df = pd.DataFrame({
    "month":    ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "sales":    [5000, 2000, 4500, 2500, 6000, 3000]
})

pivot = pd.pivot_table(df, values="sales", index="category", columns="month", aggfunc="sum")

print("Pivot Table:")
print(pivot)
