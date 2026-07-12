import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["A","B","C",],
    "age":[10,20,30],
    "score":[100,50,300]
})

fig, [hist, scat, line] = plt.subplots(3,1, figsize=(10,10))

hist.bar(df["name"], df["age"], label="Histogram")
hist.set_title("Histogram")
scat.scatter(df["name"], df["score"], label="Scatter plot")
scat.set_title("Scatter plot")
line.plot(df["name"], df["age"], label="Line plot")
line.set_title("Line plot")
plt.tight_layout()
plt.show()