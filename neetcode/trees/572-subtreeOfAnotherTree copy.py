from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and not subRoot:
                return False
            if not root and subRoot:
                return False
            if root and subRoot:
                if root.val != subRoot.val:
                    return False
                return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        self.res = False

        def dfs(root, subRoot):
            if root:
                if root.val == subRoot.val:
                    # check if root and subRoot are same tree
                    if sameTree(root, subRoot):
                        self.res = True
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)

        dfs(root, subRoot)
        return self.res


tree1 = TreeNode(3, 
                 TreeNode(4, 
                          TreeNode(1), 
                          TreeNode(2)), 
                 TreeNode(5))
tree2 = TreeNode(4, 
                 TreeNode(1), 
                 TreeNode(2))
tree3 = TreeNode(3, 
                 TreeNode(4, 
                          TreeNode(1), 
                          TreeNode(2, 
                                   TreeNode(0),
                                   None)), 
                 TreeNode(5))
tree4 = TreeNode(1, 
                 TreeNode(1), 
                 None)
tree5 = TreeNode(1)

testCases = [
    (tree4, tree5), # True
    (tree1, tree2), # True
    (tree3, tree2)  # False
]

s = Solution()
for t in testCases:
    print(s.isSubtree(t[0], t[1]))