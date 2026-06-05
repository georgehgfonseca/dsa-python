# https://www.hackerrank.com/x/library/hackerrank/all/questions/1384733
# You are developing a system for a ride-hailing company that needs to identify the shortest routes between cities. The cities and roads are represented as a graph with nodes and edges.

 

# Your task is to determine all paths from the first node to the last node, identify those with the shortest length, and classify each road as being part of any shortest path or not.

 

# Example

# g_nodes = 5

# g_edges = 7

# g_from = [1, 2, 3, 4, 5, 1, 5]

# g_to = [2, 3, 4, 5, 1, 3, 3]

# g_weight = [1, 1, 1, 1, 3, 2, 1]

 

# Graph with 5 nodes connected by lines, labeled 1 to 5, with nodes 1 and 5 having 3 connecting paths.

# The traveler must go from city 1 to city 5. The shortest path length is 3 units, and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.

# Return an array of strings ["YES", "YES", "NO", "NO", "YES", "YES", "YES"], where "YES" indicates a road is part of any shortest path and "NO" indicates it is not. Roads 3 and 4 are not on any shortest path.

 

# Function Description

# Complete the function classifyEdges in the editor with the following parameter(s):

#     int g_nodes:  the number of nodes

#     int g_from[g_edges]: one end of each  road

#     int g_to[g_edges]:  the other end of each road

#     int g_weight[g_edges]:  the length of each road

 

# Returns

#    string[g_edges]: the value at the ith index is "YES" if the ith edge is a part of a shortest path from vertex 1 to vertex g_nodes. Otherwise, it should contain "NO".

 

 

# Constraints

# 2 ≤ g_nodes ≤ 3000
# 1 ≤ g_edges ≤ min(105, (g_nodes x g_nodes - 1)/2)
# 1 ≤ g_weight[i] ≤ 105 
# 1 ≤ g_from[i], g_to[i] ≤ g_nodes
# There is at most one edge between any pair of g_nodes. 
# The graph is connected.

#
# Complete the 'classifyEdges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
import heapq

def classifyEdges(g_nodes, g_from, g_to, g_weight):
    graph = {i + 1: dict() for i in range(g_nodes)}
    for i in range(len(g_from)):
        u, v, w = g_from[i], g_to[i], g_weight[i]
        graph[u][v] = w
        graph[v][u] = w
        
    def dijkstra(source, target):
        dist = {i + 1: float("inf") for i in range(g_nodes)}
        dist[source] = 0
        heap = [(0, source)]
        closed = set()
        while heap:
            node_dist, node = heapq.heappop(heap)
            closed.add(node)
            for neigh in graph[node]:
                if neigh not in closed and dist[neigh] > dist[node] + graph[node][neigh]:
                    dist[neigh] = dist[node] + graph[node][neigh]
                    heapq.heappush(heap, (dist[neigh], neigh))
                    
        return dist
    
    
    source, target = 1, g_nodes
    dist_from_s = dijkstra(source, target)
    dist_from_t = dijkstra(target, source)
    min_dist = dist_from_s[target]
    
    res = []
    for i in range(len(g_from)):
        u, v, w = g_from[i], g_to[i], g_weight[i]
        edge_in_shortest_path = dist_from_s[u] + w + dist_from_t[v] == min_dist or dist_from_s[v] + w + dist_from_t[u] == min_dist
        res.append("YES" if edge_in_shortest_path else "NO")
        
    return res
        

def classifyEdges2(g_nodes, g_from, g_to, g_weight):
    # Build adjacency list
    adj = [[] for _ in range(g_nodes + 1)]
    for i in range(len(g_from)):
        u, v, w = g_from[i], g_to[i], g_weight[i]
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra's algorithm
    def dijkstra(start):
        dist = [float('inf')] * (g_nodes + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    # Shortest distances from node 1
    dist_from_start = dijkstra(1)
    # Shortest distances to node g_nodes (by running from g_nodes)
    dist_to_end = dijkstra(g_nodes)
    
    shortest_distance = dist_from_start[g_nodes]
    
    # Check each edge if it's on any shortest path
    result = []
    for i in range(len(g_from)):
        u, v, w = g_from[i], g_to[i], g_weight[i]
        # Edge is on shortest path if going through it gives the shortest distance
        if dist_from_start[u] + w + dist_to_end[v] == shortest_distance:
            result.append("YES")
        elif dist_from_start[v] + w + dist_to_end[u] == shortest_distance:
            result.append("YES")
        else:
            result.append("NO")
    
    return result
   
