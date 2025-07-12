from typing import List
import random
import math

class Solution:
    def kmeans(self, k: int, nodes: List[List[float]], max_iter: int = 100) -> List[List[float]]:
        # Randomly initialize centroids from nodes
        centroids = random.sample(nodes, k)

        for _ in range(max_iter):
            # Assign nodes to closest centroids
            node_assignments = {}  # idxNode: idxCluster
            for i, node in enumerate(nodes):
                distances = [math.dist(node, centroid) for centroid in centroids]
                closest = distances.index(min(distances))
                node_assignments[i] = closest

            # Recalculate centroids
            new_centroids = [[0, 0] for _ in range(k)]
            counts = [0] * k
            for i, cluster_idx in node_assignments.items():
                new_centroids[cluster_idx][0] += nodes[i][0]
                new_centroids[cluster_idx][1] += nodes[i][1]
                counts[cluster_idx] += 1

            for j in range(k):
                if counts[j] > 0:
                    new_centroids[j][0] /= counts[j]
                    new_centroids[j][1] /= counts[j]
                else:
                    # Reinitialize centroid if no points assigned
                    new_centroids[j] = random.choice(nodes)

            # Check convergence (no centroid change)
            if all(math.isclose(new_centroids[i][0], centroids[i][0], rel_tol=1e-6) and
                   math.isclose(new_centroids[i][1], centroids[i][1], rel_tol=1e-6)
                   for i in range(k)):
                break

            centroids = new_centroids

        return centroids, node_assignments

# Test
testCases = [(3, [
    [1.00, 0.52],
    [0.97, 0.56],
    [0.93, 0.53],
    [0.95, 0.57],
    [0.56, 0.04],
    [0.61, 0.00],
    [0.66, 0.07],
    [0.74, 0.26],
    [0.05, 0.89],
    [0.08, 1.00],
    [0.03, 0.81],
    [0.00, 0.89],
])]

s = Solution()
for t in testCases:
    print(s.kmeans(t[0], t[1]))


# from typing import List
# import random

# class Solution:
#     def kmeans(self, k: int, nodes: List[List[int]]) -> List[List[int]]:
#         # randomly assign centroids
#         centroids = []
#         for _ in range(k):
#             centroids.append([random.random(), random.random()])

#         sse = float("inf")
#         while True:
#             # assign nodes to closest centroids
#             node_assignments = dict() # idxNode: idxCluster
#             for i, node in enumerate(nodes):
#                 minDist = float("inf")
#                 minJ = -1
#                 for j, centroid in enumerate(centroids):
#                     # calculate euclidean distance
#                     dist = (((node[0] - centroid[0]) ** 2) + ((node[1] - centroid[1]) ** 2)) ** (1/2)
#                     if dist < minDist:
#                         minDist = dist
#                         minJ = j
#                 node_assignments[i] = minJ
            
#             # recalculate centroids
#             updatedCentroids = []
#             for j in range(k):
#                 sumX, sumY, count = 0, 0, 0
#                 for i in node_assignments:
#                     if node_assignments[i] == j:
#                         sumX += nodes[i][0]
#                         sumY += nodes[i][1]
#                         count += 1
#                 if count != 0:
#                     updatedCentroids.append([sumX / count, sumY / count])
#                 else:
#                     updatedCentroids.append([0, 0])
#             centroids = updatedCentroids

#             # calculate SSE
#             updatedSSE = 0
#             for i in node_assignments:
#                 j = node_assignments[i]
#                 error = ((nodes[i][0] - centroids[j][0]) ** 2) + ((nodes[i][1] - centroids[j][1]) ** 2)
#                 updatedSSE += error
#             if updatedSSE == sse:
#                 return sse
#             sse = updatedSSE
#             print(sse)

        

# testCases = [(3, [
# [1.00, 0.52],
# [0.97, 0.56],
# [0.93, 0.53],
# [0.95, 0.57],
# [0.56, 0.04],
# [0.61, 0.00],
# [0.66, 0.07],
# [0.74, 0.26],
# [0.05, 0.89],
# [0.08, 1.00],
# [0.03, 0.81],
# [0.00, 0.89],
# ])]

# s = Solution()
# for t in testCases:
#     print(s.kmeans(t[0], t[1]))