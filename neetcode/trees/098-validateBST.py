from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, minBound, maxBound):
            if root:
                if root.val <= minBound or root.val >= maxBound:
                    return False
                return dfs(root.left, minBound, root.val) and dfs(root.right, root.val, maxBound)
            return True
        return dfs(root, float("-inf"), float("inf"))
    
        # O(n^2) solution - accepted but not optimal
        # def getLargest(root):
        #     if root:
        #         return max(root.val, getLargest(root.left), getLargest(root.right))
        #     return float("-inf")

        # def getSmallest(root):
        #     if root:
        #         return min(root.val, getSmallest(root.left), getSmallest(root.right))
        #     return float("inf")
        
        # def dfs(root):
        #     if root:
        #         # has left child and it is not BST valid
        #         if root.left and getLargest(root.left) >= root.val:
        #             return False
        #         # has right child and it is not BST valid
        #         if root.right and root.val >= getSmallest(root.right):
        #             return False
        #         return dfs(root.left) and dfs(root.right)
                
        #     return True
        
        # return dfs(root)


tree0 = TreeNode(3, 
                 TreeNode(1,
                          TreeNode(0),
                          TreeNode(2)), 
                 TreeNode(5, 
                          TreeNode(4),
                          TreeNode(6)))
tree1 = TreeNode(2, 
                 TreeNode(1), 
                 TreeNode(3))
tree2 = TreeNode(2, 
                 TreeNode(2), 
                 TreeNode(2))
tree3 = TreeNode(5, 
                 TreeNode(1), 
                 TreeNode(4, 
                          TreeNode(3), 
                          TreeNode(6)))

testCases = [
    tree0, # True
    tree1, # True
    tree2, # False
    tree3, # False
]

s = Solution()
for t in testCases:
    print(s.isValidBST(t))


s = "abc"
s = s.replace("a", "A")
print(s)

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
for elem in queue:
    print(elem)
for i in range(len(queue)):
    print(i)