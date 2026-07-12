import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Filter: sepal length > 5 AND species is setosa
df_filtered = df[(df["sepal length (cm)"] > 5) & (df["species"] == "setosa")]

print("Rows where sepal_length > 5 and species == setosa:")
print(df_filtered)
