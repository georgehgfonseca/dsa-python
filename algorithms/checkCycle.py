from collections import defaultdict

def has_cycle(graph):
    def dfs(node, visited, parent):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True

        return False

    # Initialize data structures
    visited = defaultdict(bool)

    # Perform DFS for each node in the graph
    for node in graph:
        if not visited[node]:
            if dfs(node, visited, None):
                return True

    return False

# Example usage:
# Define a graph as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

# Check if the graph has a cycle
has_cycle_result = has_cycle(graph)

print("Does the graph have a cycle?", has_cycle_result)