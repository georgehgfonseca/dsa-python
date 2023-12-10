from typing import Optional, List

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        res = list()
        curr_max = float("-inf")

        def dfs(root, curr_max):
            if root:
                if root.val >= curr_max:
                    res.append(root.val)
                    curr_max = root.val
                dfs(root.left, curr_max)
                dfs(root.right, curr_max)

        dfs(root, curr_max)
        return len(res)


# root:  
# left:  
# right: 
# res:   [[3], [9, 20], [15, 7], []]
# level: 3
# (3, 1) (9, 2) (20, 2) (15, 3) (7, 3)

tree1 = TreeNode(3, 
                 TreeNode(1, 
                          TreeNode(3), 
                          None), 
                 TreeNode(4, 
                          TreeNode(1), 
                          TreeNode(5)))

testCases = [
    tree1,
]

s = Solution()
for t in testCases:
    print(s.goodNodes(t))