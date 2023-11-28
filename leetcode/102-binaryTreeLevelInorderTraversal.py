from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def helper(root, level, ans):
            if root:
                if level + 1 > len(ans):
                    ans.append([])
                ans[level].append(root.val)
                helper(root.left, level + 1, ans)
                helper(root.right, level + 1, ans)

        ans = []
        helper(root, 0, ans)
        return ans

        

t1 = TreeNode(3, 
              TreeNode(9), 
              TreeNode(20, 
                       TreeNode(15), 
                       TreeNode(7)))

testCases = [t1]
s = Solution()
for t in testCases:
    print(s.levelOrder(t))
