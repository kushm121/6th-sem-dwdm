import numpy as np

data = np.array([
    [2.0, 10.0],
    [2.0, 6.0],
    [11.0, 11.0],
    [6.0, 9.0],
    [6.0, 4.0],
    [1.0, 2.0],
    [5.0, 10.0],
    [4.0, 9.0],
    [10.0, 12.0],
    [7.0, 5.0],
    [9.0, 11.0],
    [4.0, 6.0],
    [3.0, 10.0],
    [3.0, 8.0],
    [6.0, 11.0]
])

k = 3

def distance(point1, point2):
    return np.sqrt(np.sum(point1 - point2) ** 2)

def assign_clusters(data, centroids):
    clusters  = [[] for i in range(len(centroids))]
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        min_index = np.argmin(distances)
        clusters[min_index].append(point)

    return clusters

def update_centroids(clusters):
    centroids = []
    for cluster in clusters:
        if cluster:
            centroids.append(np.mean(cluster, axis=0))

    return np.array(centroids)

def k_means(data, k, max_iterations = 10):
    centroids = np.array([
        [1.0, 2.0],
        [6.0, 9.0],
        [10.0, 12.0]
    ])

    for i in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids

    return centroids, clusters


centroids, clusters = k_means(data, k)

print("centroids: ")
for i in centroids:
    print(i)

print("\nclusters: ")
for i in clusters:
    print(i)
