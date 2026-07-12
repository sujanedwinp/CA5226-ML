import pandas as pd
data = {
    "Name": ["A", "R", "P"],
    "Marks":[85, 72, 90],
    "Grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)
print(df)
