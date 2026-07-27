
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C"],
    "Age": [25, 30, 22]
}

data= pd.DataFrame(data)

print(data.describe())

plt.bar(data["Name"], data["Age"])
plt.show()
