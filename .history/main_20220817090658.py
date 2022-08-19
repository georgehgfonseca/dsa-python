from binaryTree import TreeNode

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
