import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

# Load dataset
data = pd.DataFrame({
    "x1": [1, 2, 3, 4, 5, 6],
    "x2": [35, 45, 50, 60, 70, 85]
})

# construct the distance matrix (Euclidean distance between every pair of points)
dist_matrix = squareform(
    pdist(
        data, 
        metric="euclidean"
    ))

print("Distance matrix:\n", 
      pd.DataFrame(dist_matrix), 
      "\n"
    )

# Create and Train
model = AgglomerativeClustering(n_clusters=2, linkage="single")
data["cluster"] = model.fit_predict(data)
print("Data with assigned clusters:\n", data)

# plot the dendrogram (uses single linkage on the same distances)
Z = linkage(data[["x1", "x2"]], method="single")

plt.figure()
dendrogram(Z, labels=[f"P{i}" for i in data.index])
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()
