from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        pass


tree1 = TreeNode(1, 
                 TreeNode(2), 
                 TreeNode(3))
tree2 = TreeNode(1, 
                 TreeNode(2), 
                 TreeNode(3))
tree3 = TreeNode(1, 
                 TreeNode(2), 
                 None)
tree4 = TreeNode(1, 
                 None, 
                 TreeNode(2))

testCases = [
    (tree1, tree2), # True
    (tree3, tree4)  # False
]

s = Solution()
for t in testCases:
    print(s.isSameTree(t[0], t[1]))