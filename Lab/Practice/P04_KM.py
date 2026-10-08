import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 45, 50, 60, 70, 85, 90, 75, 70, 60]
})

X=data[["StudyHours", "Marks"]]

model=KMeans(n_clusters=2, random_state=0, n_init=10)
data["cluster"]=model.fit_predict(X)

print("cd\n", data)
print("cc\n", model.cluster_centers_)

plt.scatter(data["StudyHours"],data["Marks"], c=data["cluster"])
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=200
)
plt.title("KM")
plt.show()