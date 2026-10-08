import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering as AC
from scipy.spatial.distance import squareform, pdist
from scipy.cluster.hierarchy import linkage, dendrogram

data = pd.DataFrame({
    "x1": [1, 2, 3, 4, 5, 6],
    "x2": [35, 45, 50, 60, 70, 85]
})

dist=squareform(pdist(data))
print("dist\n", pd.DataFrame(dist))

model=AC(n_clusters=2, linkage="single")
data["cluster"]=model.fit_predict(data)
print("Data with the assinging cluster\n", data)

z=linkage(data[["x1", "x2"]], method="single")
dendrogram(z, labels=[f"P{i}" for i in data.index])
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()
