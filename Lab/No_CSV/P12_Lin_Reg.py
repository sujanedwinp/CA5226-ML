import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

data = pd.DataFrame({
    "Years_Experience": [
        4.4, 9.6, 7.6, 6.4, 2.4, 2.4, 1.5, 8.8, 6.4, 7.4,
        1.2, 9.7, 8.5, 2.9, 2.6, 2.7, 3.7, 5.7, 4.9, 3.6
    ],
    "Salary_USD": [
        63300, 112900, 91000, 78800, 56300, 49500, 43000, 99100, 82200, 93300,
        35600, 114000, 99800, 53500, 49700, 60400, 61400, 74200, 74900, 55700
    ]
})

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
