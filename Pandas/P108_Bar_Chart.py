import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B", "C", "A", "B"]
})

values = df["category"].value_counts()
values.plot(kind="bar", color=["red", "green", "blue"])

plt.title("Counts of Unique Values in 'category'")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
