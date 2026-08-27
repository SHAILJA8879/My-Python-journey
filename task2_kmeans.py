import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Fit the model and get cluster labels
clusters = kmeans.fit_predict(X)

# Plot the K-Means clusters
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=clusters
)

plt.title("K-Means Clustering of Iris (k=3)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()
# Plot the actual Iris species
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y
)

plt.title("Actual Iris Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()