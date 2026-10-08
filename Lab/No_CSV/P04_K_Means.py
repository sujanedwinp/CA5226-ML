import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 45, 50, 60, 70, 85, 90, 75, 70, 60]
})

X = data[["StudyHours", "Marks"]]

# 1*
# Create and Train
model = KMeans(n_clusters=2, random_state=0, n_init=10)
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



# 1* --------------------------------
# Create K-Means model

#   ### 3. The One Big Difference: Initial Centers (init=...)
#  Difference from nates
#   Look at this line in the new program:
#     kmeans = KMeans(n_clusters=2, init=[[2, 1], [2, 3]],
#   n_init=1)
#   • When to use this: Many university lab questions say:
#   │ "Given points ..., take initial cluster centers v₁ = (2, 1)
#   │ and v₂ = (2, 3) and find the final clusters."
#   │ If your exam question explicitly mentions starting centers,
#   │ you must pass init=[[2, 1], [2, 3]], n_init=1 like in your
#   │ new program!
#   • If no centers are given: P04's approach
#   (KMeans(n_clusters=2)) is preferred because scikit-learn
#   chooses the optimal starting points automatically.
#   ──────