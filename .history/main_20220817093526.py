from binaryTree import TreeNode
from graph import Graph

# root1 = TreeNode(2, TreeNode(1))
# root2 = TreeNode(3, TreeNode(2), TreeNode(5))
# root3 = TreeNode(5, TreeNode(4))
# trees = [root1, root2, root3]

tree = TreeNode(2)
tree.addNode(tree, 5)
tree.addNode(tree, 4)
tree.addNode(tree, 1)
tree.addNode(tree, 7)
print(tree.traversePostorder(tree))

graph = Graph(6)
graph.addUndirectedEdge(0, 1)
graph.addUndirectedEdge(0, 3)
graph.addUndirectedEdge(3, 2)
graph.addUndirectedEdge(1, 4)
graph.addUndirectedEdge(2, 4)
graph.addUndirectedEdge(1, 5)
