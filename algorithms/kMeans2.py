import random
import math
from typing import List
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, k: int, max_iterations: int = 100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = []

    def kmeans_plus_plus_init(self, data, k):
        centroids = []
        centroids.append(random.choice(data))  # Step 1

        while len(centroids) < k:
            distances = []
            for point in data:
                # Find distance to nearest existing centroid
                min_dist = min(self.euclidean_distance(point, c) for c in centroids)
                distances.append(min_dist ** 2)  # Step 2

            total = sum(distances)
            probs = [d / total for d in distances]  # Step 3

            # Choose next centroid with weighted probability
            r = random.random()
            cumulative = 0
            for point, p in zip(data, probs):
                cumulative += p
                if r < cumulative:
                    centroids.append(point)
                    break

        return centroids

    def initialize_centroids(self, data: List[List[float]]) -> None:
        # self.centroids = random.sample(data, self.k)
        self.centroids = self.kmeans_plus_plus_init(data, self.k)

    def euclidean_distance(self, point1: List[float], point2: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

    def assign_clusters(self, data: List[List[float]]) -> List[int]:
        clusters = []
        for point in data:
            distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
            clusters.append(distances.index(min(distances)))
        return clusters

    def update_centroids(self, data: List[List[float]], clusters: List[int]) -> None:
        new_centroids = [[0] * len(data[0]) for _ in range(self.k)]
        counts = [0] * self.k

        for point, cluster in zip(data, clusters):
            for i in range(len(point)):
                new_centroids[cluster][i] += point[i]
            counts[cluster] += 1

        for i in range(self.k):
            if counts[i] > 0:
                self.centroids[i] = [x / counts[i] for x in new_centroids[i]]

    def fit(self, data: List[List[float]]) -> List[int]:
        self.initialize_centroids(data)

        for _ in range(self.max_iterations):
            clusters = self.assign_clusters(data)
            prev_centroids = [c[:] for c in self.centroids]
            self.update_centroids(data, clusters)

            if prev_centroids == self.centroids:
                break

        return clusters

    def plot_clusters(self, data: List[List[float]], clusters: List[int]) -> None:
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        for i in range(self.k):
            cluster_points = [point for point, c in zip(data, clusters) if c == i]
            xs, ys = zip(*cluster_points)
            plt.scatter(xs, ys, c=colors[i % len(colors)], label=f"Cluster {i+1}")

        # Plot centroids
        cent_x, cent_y = zip(*self.centroids)
        plt.scatter(cent_x, cent_y, c='black', marker='X', s=200, label='Centroids')
        plt.legend()
        plt.title("K-Means Clustering")
        plt.savefig("kmeans_result.png")
        print("Plot saved as kmeans_result.png")

if __name__ == "__main__":
    data = [
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ]

    kmeans = KMeans(k=3)
    cluster_assignments = kmeans.fit(data)

    print("Cluster Assignments:", cluster_assignments)
    print("Centroids:", kmeans.centroids)

    kmeans.plot_clusters(data, cluster_assignments)
