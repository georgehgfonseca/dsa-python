from typing import Optional, List

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # compute the level order tree
        level_order = [[]]

        def dfs(root, level):
            if root:
                level_order[level - 1].append(root.val)
                level += 1
                if level > len(level_order):
                    level_order.append([])

                dfs(root.left, level)
                dfs(root.right, level)

        dfs(root, 1)
        level_order.pop()

        # get the last element of each level
        res = []
        for order in level_order:
            res.append(order[-1])
         
        return res


# root:  
# left:  
# right: 
# res:   [[3], [9, 20], [15, 7], []]
# level: 3
# (3, 1) (9, 2) (20, 2) (15, 3) (7, 3)

tree1 = TreeNode(1, 
                 TreeNode(2, 
                          None, 
                          TreeNode(5)), 
                 TreeNode(3, 
                          None, 
                          TreeNode(4)))
tree2 = TreeNode(3, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15), 
                          TreeNode(7)))
tree3 = TreeNode(1, 
                 TreeNode(2), 
                 None)
tree4 = TreeNode(1, 
                 TreeNode(2, 
                          TreeNode(4), 
                          None), 
                 TreeNode(3))

testCases = [
    tree1,
    tree2,
    tree3,
]

s = Solution()
for t in testCases:
    print(s.rightSideView(t))