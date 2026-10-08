import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

data=pd.read_csv("./Lab/P12_Lin_Reg/sample_dataset.csv")

X=data[[data.columns[0]]]
Y=data[data.columns[1]]

model=LR()
model.fit(X, Y)

Y_pred= model.predict(X)

print("Slope:", model.coef_[0]) # m
print("Intercept", model.intercept_) # c

plt.scatter(X,Y)
plt.plot(X, Y_pred)

plt.title("Simple Lin Reg")
plt.xlabel(data.columns[1])
plt.ylabel(data.columns[0])

plt.show()