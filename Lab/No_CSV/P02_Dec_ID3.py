import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

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

# print("Training Data:")
# print(data)

# Separate input and output
X = data.drop("PlayTennis", axis=1)
Y = data["PlayTennis"]

# Convert text values into numbers
X_LE = {}
for column in X.columns:
    X_LE[column] = LabelEncoder()
    X[column] = X_LE[column].fit_transform(X[column])
print(X_LE)

Y_LE = LabelEncoder()
Y = Y_LE.fit_transform(Y)

# Create ID3 decision tree and rain the model
model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=0
)

model.fit(X, Y)

# Display tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=Y_LE.classes_,
    filled=True
)

plt.title("Decision Tree using ID3")
plt.show()

# New sample
new_sample = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["Normal"],
    "Wind": ["Strong"]
})

# Convert new sample using the same X_LE
for column in new_sample.columns:
    new_sample[column] = X_LE[column].transform(new_sample[column])

# Classify new sample
prediction = model.predict(new_sample)

print("New Sample:")
print(new_sample)

print("Prediction:", Y_LE.inverse_transform(prediction)[0])
