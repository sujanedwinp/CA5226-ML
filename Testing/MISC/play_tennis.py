import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Load the dataset
# ------------------------------------------------------------

df = pd.read_csv("playtennis.csv")

print("Dataset:\n")
print(df)

# Day is only an identifier, so we don't use it.
features = ["outlook", "temperature", "humidity", "wind"]
target = "playtennis"


# ------------------------------------------------------------
# Encode categorical values into numbers
# ------------------------------------------------------------

encoders = {}

X = pd.DataFrame()

for col in features:
    le = LabelEncoder()
    X[col] = le.fit_transform(df[col])
    encoders[col] = le

# Encode target values: no/yes -> numbers
y_encoder = LabelEncoder()
y = y_encoder.fit_transform(df[target])


# ------------------------------------------------------------
# Build the Decision Tree using ID3
# criterion="entropy" means the tree uses entropy
# and information gain to choose the best attribute.
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=0
)

model.fit(X, y)


# ------------------------------------------------------------
# Print the Decision Tree
# ------------------------------------------------------------

print("\nDecision Tree (ID3):\n")

print(
    export_text(
        model,
        feature_names=features
    )
)


# ------------------------------------------------------------
# Check training accuracy
# ------------------------------------------------------------

predicted = model.predict(X)

correct = sum(predicted == y)

print(
    f"Training accuracy: {correct}/{len(y)}"
)


# ------------------------------------------------------------
# Predict a new sample
# ------------------------------------------------------------

sample = {
    "outlook": "sunny",
    "temperature": "cool",
    "humidity": "normal",
    "wind": "weak"
}

sample_df = pd.DataFrame([sample])


sample_encoded = pd.DataFrame()

for col in features:
    sample_encoded[col] = encoders[col].transform(
        sample_df[col]
    )


prediction = model.predict(sample_encoded)

prediction = y_encoder.inverse_transform(prediction)

print(
    f"\nPredict {sample} -> {prediction[0]}"
)

plt.figure(figsize=(12, 8))

plot_tree(
    model,
    feature_names=features,
    class_names=y_encoder.classes_,
    filled=True
)

plt.savefig(
    "decision_tree.png",
    bbox_inches="tight",
    dpi=150
)

print("\nTree diagram saved as decision_tree.png")