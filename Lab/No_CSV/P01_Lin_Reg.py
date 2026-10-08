import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR


data = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5], 
    "Calories": [150, 260, 340, 430, 520]
})

X=data[[data.columns[0]]]
Y=data[data.columns[1]]

model=LR()
model.fit(X, Y)

m= model.coef_[0]
c= model.intercept_
print("Slope:", m) # m
print("Intercept", c) # c
print(f"Regression equation: y = {m}x + {c}")

X_pred = 6
Y_pred= model.predict([[X_pred]])[0]

plt.scatter(X,Y)
plt.plot(X, model.predict(X))
plt.scatter(X_pred,Y_pred)

plt.title("Simple Lin Reg")
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.legend()
plt.grid(True)
plt.show()
