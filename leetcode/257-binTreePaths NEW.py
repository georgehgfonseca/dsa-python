from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def arrToPath(arr):
            path = str(arr[0])
            for i in range(1, len(arr)):
                path += "->" + str(arr[i])
            return path

        def helper(root, currPath, paths):
            if root:
                if not root.left and not root.right:
                    # Leaf node
                    paths.append(arrToPath(currPath + [root.val]))
                # Move to children
                helper(root.left, currPath + [root.val], paths)
                helper(root.right, currPath + [root.val], paths)

        paths = []
        helper(root, [], paths)
        return paths


t = TreeNode(1, 
             TreeNode(2, 
                      None, 
                      TreeNode(5, 
                               None, 
                               None)), 
             TreeNode(3, 
                      None, 
                      None))
t2 = TreeNode(1, 
              TreeNode(2, 
                       TreeNode(4,
                                 None, 
                                 None), 
                       TreeNode(5, 
                                None, 
                                None)), 
              TreeNode(3, 
                       TreeNode(6, 
                                None, 
                                None), 
                       TreeNode(7, 
                                None, 
                                None)))
testCases = [t, t2]
s = Solution()
for t in testCases:
    print(s.binaryTreePaths(t))
