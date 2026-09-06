import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("./Lab/P14_NBD/nbd_data.csv")

# DONT WRITE THE BELOW
# print("Training Data:")
# print(data)

# Separate input and output
X = data.drop("PlayTennis", axis=1)
Y = data["PlayTennis"]

# Convert text values into numbers
encoders = {}

for column in X.columns:
    encoders[column] = LabelEncoder()
    X[column] = encoders[column].fit_transform(X[column])

target_encoder = LabelEncoder()
Y = target_encoder.fit_transform(Y)

# Create Naive Bayes classifier
model = GaussianNB()

# Train the model
model.fit(X, Y)

# Test data
test_data = pd.DataFrame({
    "Outlook": ["Sunny", "Rain", "Overcast", "Sunny"],
    "Temperature": ["Cool", "Cool", "Hot", "Hot"],
    "Humidity": ["Normal", "Normal", "High", "High"],
    "Wind": ["Strong", "Weak", "Weak", "Strong"],
    "PlayTennis": ["No", "Yes", "Yes", "No"]
})

# Separate test inputs and actual output
X_test = test_data.drop("PlayTennis", axis=1)
Y_test = test_data["PlayTennis"]

# Encode test data using the same encoders
for column in X_test.columns:
    X_test[column] = encoders[column].transform(X_test[column])

Y_test = target_encoder.transform(Y_test)

# Predict test data
Y_pred = model.predict(X_test)

# Display predictions
print("\nActual:", Y_test)
print("Predicted:", Y_pred)

# Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy:", accuracy * 100, "%")