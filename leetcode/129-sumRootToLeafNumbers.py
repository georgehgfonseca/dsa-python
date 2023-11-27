from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root, path, allPaths):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    # Root is a leaf
                    allPaths.append(path)
                    return
                helper(root.left, path[:], allPaths)
                helper(root.right, path[:], allPaths)
        
        allPaths = []
        helper(root, [], allPaths)

        overallSum = 0
        for path in allPaths:
            numberPath = 0
            i = 0
            while i < len(path):
                numberPath += path[i] * 10**(len(path) - i - 1)
                i += 1
            overallSum += numberPath
        return overallSum


t1 = TreeNode(1, 
              TreeNode(2, 
                       TreeNode(3), 
                       TreeNode(4)), 
              TreeNode(2, 
                       TreeNode(4), 
                       TreeNode(3))) 
t2 = TreeNode(4, 
              TreeNode(9, 
                       TreeNode(5), 
                       TreeNode(1)), 
              TreeNode(0)) 
testCases = [t1, t2]
s = Solution()
for t in testCases:
    print(s.sumNumbers(t))
