import pandas as pd
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.naive_bayes import CategoricalNB as CNB

data = pd.DataFrame({
    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain"
    ],
    "Temperature": [
        "Hot", "Hot", "Hot", "Hot", "Cool", "Cool"
    ],
    "Humidity": [
        "High", "High", "High", "High", "Normal", "Normal"
    ],
    "Wind": [
        "Weak", "Strong", "Weak", "Weak", "Weak", "Strong"
    ],
    "PlayTennis": [
        "No", "No", "Yes", "Yes", "Yes", "No"
    ]
})

X=data.drop("PlayTennis", axis=1)
Y=data["PlayTennis"]

XLE={}
for col in X.columns:
    XLE[col]=LE()
    X[col]=XLE[col].fit_transform(X[col])

YLE=LE()
Y=YLE.fit_transform(Y)

model=CNB()
model.fit(X, Y)


test_data = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["Normal"],
    "Wind": ["Strong"],
    "PlayTennis": ["Yes"]
})

X_test=test_data.drop("PlayTennis", axis=1)
Y_test=test_data["PlayTennis"]

for col in X_test.columns:
    X_test[col]=XLE[col].transform(X_test[col])

Y_test=YLE.transform(Y_test)
Y_pred=model.predict(X_test)

print("Actual: ", Y_test)
print("Pred: ", Y_pred)
