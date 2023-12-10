from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # convert tree to an array
        self.treeArr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.treeArr.append(node.val)
            if len(self.treeArr) == k:
                # save needles iterations
                return
            dfs(node.right)

        dfs(root)

        return self.treeArr[k-1]


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
