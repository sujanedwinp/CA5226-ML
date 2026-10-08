from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.model_selection import train_test_split as tts

iris=load_iris()
X=iris.data
Y=iris.target

X_train, X_test, Y_train, Y_test = tts(
    X, Y, test_size=0.2, random_state=42
)

model=KNC(n_neighbors=5)
model.fit(X_train, Y_train)

accuracy=model.score[X_test, Y_test]
print(accuracy)

sample=[[45, 50, 60, 75]]
pred=model.predict(sample)
print(pred[0])