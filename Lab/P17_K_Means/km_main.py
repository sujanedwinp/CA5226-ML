import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("./Lab/P17_K_Means/km_data.csv")

print("Data:")
print(data)

# Select features
X = data[["StudyHours", "Marks"]]

# Create K-Means model
model = KMeans(n_clusters=2, random_state=0, n_init=10)

# Train the model and assign clusters
data["Cluster"] = model.fit_predict(X)

# Display clustered data
print("\nClustered Data:")
print(data)

# Display cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)

# Plot clusters
plt.scatter(
    data["StudyHours"],
    data["Marks"],
    c=data["Cluster"]
)

# Plot cluster centers
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()