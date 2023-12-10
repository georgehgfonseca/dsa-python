from typing import Optional, List

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = {preorder[i]: i for i in range(len(preorder))} 
        inorder_index = {inorder[i]: i for i in range(len(inorder))} 

        def helper(i, leftArray, rightArray):
            if not leftArray and not rightArray:
                return None
            mid = inorder_index[preorder[i]]
            return TreeNode(preorder[i], helper(i+1, inorder[:mid-1]), helper(i+2, inorder[mid+1:]))

        return helper(0, inorder, inorder)




testCases = [
    ([3,9,20,15,7], [9,3,15,20,7])
]

s = Solution()
for t in testCases:
    print(s.buildTree(t[0], t[1]))
