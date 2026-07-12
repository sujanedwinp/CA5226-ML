import pandas as pd

df = pd.DataFrame({
    "name": ["Rahul", "Sam", "Raj", "Tom"],
    "department": ["HR", "IT", "HR", "Sales"]
})

print("Before Encoding:")
print(df)

df_encoded = pd.get_dummies(df, columns=["department"])

print("\nAfter Encoding:")
print(df_encoded)