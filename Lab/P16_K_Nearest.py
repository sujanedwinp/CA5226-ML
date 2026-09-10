from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=5)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Count correct and wrong predictions
correct = sum(y_test == y_pred)
wrong = sum(y_test != y_pred)

# Print summary
print("Correct predictions:", correct)
print("Wrong predictions:", wrong)


# -------------------------------------------------
# ONLY IF YOU WANT TO PRINT ALL
# -------------------------------------------------
# 
# # Print correct and wrong predictions
# for actual, predicted in zip(y_test, y_pred):
#     if actual == predicted:
#         print("Correct: Actual =", iris.target_names[actual],
#               "Predicted =", iris.target_names[predicted])
#     else:
#         print("Wrong: Actual =", iris.target_names[actual],
#               "Predicted =", iris.target_names[predicted])