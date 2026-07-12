import pandas as pd

nums=[10, 20, 30, 40, 50]

s=pd.Series(nums)
print(f"{s}\n{s.index}\n{s.values}")