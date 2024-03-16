from collections import deque

def has_cycle(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if bfs_cycle(graph, node, visited):
                return True
    return False

def bfs_cycle(graph, start, visited):
    queue = deque([(start, None)])  # (node, parent)

    while queue:
        node, parent = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor in visited:
                if neighbor != parent:
                    return True  # Cycle detected
            else:
                queue.append((neighbor, node))

    return False

# Example usage:
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: [1]  # introducing a cycle (4 -> 1)
}

if has_cycle(graph):
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")