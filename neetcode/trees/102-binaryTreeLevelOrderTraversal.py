from typing import Optional, List

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [[]]

        def dfs(root, level):
            if root:
                res[level - 1].append(root.val)
                level += 1
                if level > len(res):
                    res.append([]) 
                dfs(root.left, level)
                dfs(root.right, level)

        dfs(root, 1)
        res.pop()

        return res


# root:  
# left:  
# right: 
# res:   [[3], [9, 20], [15, 7], []]
# level: 3
# (3, 1) (9, 2) (20, 2) (15, 3) (7, 3)

tree1 = TreeNode(3, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15), 
                          TreeNode(7)))

testCases = [
    tree1
]

s = Solution()
for t in testCases:
    print(s.levelOrder(t))