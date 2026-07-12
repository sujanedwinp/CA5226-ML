import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Var": ["A","B","C","D"],
    "Val": [x**2 for x in range(1,5)]
})

df["ValSq"] = df["Val"].apply(np.sqrt)
print(df)