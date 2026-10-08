from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNC

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN model
model = KNC(n_neighbors=5)
model.fit(X_train, y_train)

# Predict
accuracy = model.score(X_test, y_test)
print("Accuracy", accuracy)

sample=[[45, 50, 60, 75]]
pred = model.predict(sample)
print("Preds", pred[0])
