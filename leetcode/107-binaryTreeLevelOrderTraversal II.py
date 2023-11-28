from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        def helper(root, level, ans):
            if root:
                if level + 1 > len(ans):
                    ans.append([])
                ans[level].append(root.val)
                helper(root.left, level + 1, ans)
                helper(root.right, level + 1, ans)

        ans = []
        helper(root, 0, ans)

        # Reverse ans order (without additional space)
        start = 0
        end = len(ans) - 1
        while start < end:
            ans[start], ans[end] = ans[end], ans[start]
            start += 1
            end -= 1
        return ans

        # # Reverse ans order
        # ans_temp = []
        # for i in range(len(ans) - 1, -1, -1):
        #     ans_temp.append(ans[i])
        # return ans_temp
        

t1 = TreeNode(3, 
              TreeNode(9), 
              TreeNode(20, 
                       TreeNode(15), 
                       TreeNode(7)))

testCases = [t1]
s = Solution()
for t in testCases:
    print(s.levelOrderBottom(t))
