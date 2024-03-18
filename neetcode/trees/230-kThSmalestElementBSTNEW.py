from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # convert tree to an array
        tree_arr = []

        def inorder_traverse(root):
            if root:
                inorder_traverse(root.left)
                tree_arr.append(root.val)
                inorder_traverse(root.right)

        inorder_traverse(root)
        return tree_arr[k - 1]


tree1 = TreeNode(3, 
                 TreeNode(1,
                          None,
                          TreeNode(2)), 
                 TreeNode(4, 
                          None,
                          None))

testCases = [
    (tree1, 1), 
]

s = Solution()
for t in testCases:
    print(s.kthSmallest(t[0], t[1]))
