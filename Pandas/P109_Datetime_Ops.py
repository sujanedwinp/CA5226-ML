import pandas as pd

df = pd.DataFrame({
    "event": ["A", "B", "C", "D"],
    "date":  ["2024-01-15", "2024-03-22", "2024-06-05", "2024-11-30"]
})

df["date_datetime"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
df["month"] = df["date"].dt.month
print(df)
