
import pandas as pd

data = [
    ["A", 25],
    ["B", 30],
    ["C", 22]
]
df = pd.DataFrame(data, columns=["Name", "Age"])

print(df)