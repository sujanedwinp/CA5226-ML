import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start="2026-01-01", periods=30, freq="B")
prices = 100 + np.cumsum(np.random.randn(30))

df = pd.DataFrame({"date": dates, "price": prices})
df.set_index("date", inplace=True)

df["daily_return"] = df["price"].pct_change()
print(df.head(10))

fig, (price_plot, dr_plot) = plt.subplots(2, 1, figsize=(8, 5))
price_plot.plot(df["price"], label="Price")
price_plot.set_title("Stock Price")
dr_plot.bar(df.index, df["daily_return"], label="Daily Return", color="red")
dr_plot.set_title("Daily Returns")
plt.tight_layout()
plt.show()
