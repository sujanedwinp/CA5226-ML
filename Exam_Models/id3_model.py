import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Load dataset
df = pd.read_csv("playtennis.csv")

features = ["outlook", "temperature", "humidity", "wind"]
target = "playtennis"

# Encode categorical data
X = df[features].copy()

for col in features:
    X[col] = LabelEncoder().fit_transform(X[col])

y = LabelEncoder().fit_transform(df[target])

# Create ID3 tree
model = DecisionTreeClassifier(criterion="entropy", random_state=0)
model.fit(X, y)

# Print tree
print("Decision Tree:")
print(model)

# Plot tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=features,
          class_names=["No", "Yes"], filled=True)

plt.title("ID3 Decision Tree")
plt.show()