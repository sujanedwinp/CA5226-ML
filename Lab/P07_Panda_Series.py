import pandas as pd

data = [23, 34, 65, 87, 32, 78, 34]

s = pd.DataFrame(data, columns=["Values"])
s = s["Values"]
# OR instead u can do s["Values"].mean()
print("Mean:", s.mean())
print("Median:", s.median())
print("Mode:")
print(s.mode())
print("Variance:", s.var())
print("Standard Deviation:", s.std())


