from searchSort import SearchSort
from binaryTree import TreeNode
from graph import Graph
from weightedGraph import WeightedGraph

# Array algorithms
array = SearchSort([2, 4, 6, 7, 9])
print(array.isOrdered())

# Tree algorithms
tree = TreeNode(2)
tree.addNode(tree, 5)
tree.addNode(tree, 4)
tree.addNode(tree, 1)
tree.addNode(tree, 7)
print(tree.traversePreorder(tree))
print(tree.traverseOrder(tree))
print(tree.traversePostorder(tree))

# Graph algorithms
graph = WeightedGraph(6)
graph.addUndirectedEdge(0, 1, 1)
graph.addUndirectedEdge(0, 3, 1)
graph.addUndirectedEdge(3, 2, 1)
graph.addUndirectedEdge(1, 4, 1)
graph.addUndirectedEdge(2, 4, 1)
graph.addUndirectedEdge(1, 5, 1)
print(graph.toString())
print(graph.bfs(0))
print(graph.dfs(0))
print(graph.connected())
print(graph.dijkstra_pq(0, 5))
