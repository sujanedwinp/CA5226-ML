import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import accuracy_score <- ONLY FOR MULTIPLE TESTS

# Load dataset
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

X = data.drop("PlayTennis", axis=1)
Y = data["PlayTennis"]

X_LE = {}

for column in X.columns:
    X_LE[column] = LabelEncoder()
    X[column] = X_LE[column].fit_transform(X[column])

Y_LE = LabelEncoder()
Y = Y_LE.fit_transform(Y)

# Create Naive Bayes classifier and Train
model = CategoricalNB()
model.fit(X, Y)

# Tests ---
test_data = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["Normal"],
    "Wind": ["Strong"],
    "PlayTennis": ["Yes"]
})

X_test = test_data.drop("PlayTennis", axis=1)
Y_test = test_data["PlayTennis"]

for column in X_test.columns:
    X_test[column] = X_LE[column].transform(X_test[column])

Y_test = Y_LE.transform(Y_test)
Y_pred = model.predict(X_test)

print("\nActual:", Y_test)
print("Predicted:", Y_pred)

# Calculate accuracy - FOR MULTIPLE TESTS
# accuracy = accuracy_score(Y_test, Y_pred)
# print("\nAccuracy:", accuracy * 100, "%")
