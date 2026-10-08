import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("./Lab/P15_Dec_ID3/sample_dataset.csv")

print("Training Data:")
print(data)

# Separate input and output
X = data.drop("PlayTennis", axis=1)
Y = data["PlayTennis"]

# Convert text values into numbers
encoders = {}

for column in X.columns:
    encoders[column] = LabelEncoder()
    X[column] = encoders[column].fit_transform(X[column])
print(encoders)

target_encoder = LabelEncoder()
Y = target_encoder.fit_transform(Y)

# Create ID3 decision tree
model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=0
)

# Train the model
model.fit(X, Y)

# Display tree
plt.figure(figsize=(12, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=target_encoder.classes_,
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

# Convert new sample using the same encoders
for column in new_sample.columns:
    new_sample[column] = encoders[column].transform(new_sample[column])

# Classify new sample
prediction = model.predict(new_sample)

print("New Sample:")
print(new_sample)

print("Prediction:", target_encoder.inverse_transform(prediction)[0])