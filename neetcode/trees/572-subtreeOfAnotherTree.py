from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.ans = False

        def sameTree(p, q):
            if p and q:
                if p.val == q.val:
                    return sameTree(p.left, q.left) and sameTree(p.right, q.right)
                return False
            elif not p and not q:
                return True
            else:
                return False

        # try to find the root of subRoot in root
        def dfs(root, subRoot):
            if root:
                if root.val == subRoot.val:
                    # Check if they are the same tree
                    if not self.ans:
                        self.ans = sameTree(root, subRoot)
                
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)

        dfs(root, subRoot)
        return self.ans
    

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