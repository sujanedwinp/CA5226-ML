import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.tree import DecisionTreeClassifier as DTC, plot_tree

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

model=DTC(criterion="entropy", random_state=0)
model.fit(X, Y)

plot_tree(
    model,
    feature_names=X.columns,
    class_names= YLE.classes_,
    filled=True
)
plt.title("ID3")
plt.show()

ns=pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["Normal"],
    "Wind": ["Strong"]
})

for col in ns.columns:
    ns[col]=XLE[col].transform(ns[col])

Y_pred=model.predict(ns)
print(ns)
print(f"Pred: {YLE.inverse_transform(Y_pred)[0]}")
