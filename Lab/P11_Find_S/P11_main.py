import pandas as pd

data=pd.read_csv("./Lab/P11_Find_S/sample_dataset.csv")
[rows, cols]=data.shape

hypo=[-1]+['~']*(cols-1)

for i in range(rows):
    if data.iloc[i, cols-1]=='No':
        hypo[0]+=1
        continue

    hypo[0]+=1
    for j in range(1, cols):
        if hypo[j]=='~':
            # j-1 bcz hypo is already handled before and loop start from 1
            hypo[j]= data.iloc[i, j-1]
        elif hypo[j]==data.iloc[i, j-1]:
            continue
        else:
            hypo[j]= '?'

print("Most Specific hypothesis\n", hypo)
