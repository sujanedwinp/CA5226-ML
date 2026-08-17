import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("clients_data.csv")

X = data[["Exercise_Time_Hours"]]
y = data["Calories_Burned"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Get slope and intercept
m = model.coef_[0]
c = model.intercept_

print("Slope:", m)
print("Intercept:", c)
print("Equation: y =", m, "x +", c)

# Prediction
x_new = [[6]]
y_pred = model.predict(x_new)
print("Predicted calories:", y_pred[0])

# Plot
plt.scatter(X, y, label="Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.scatter(6, y_pred[0], marker="D", label="Prediction")

plt.xlabel("Exercise Time (Hours)")
plt.ylabel("Calories Burned")
plt.title("Linear Regression")
plt.legend()
plt.show()