from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # TODO: copied from solutions
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    
        # def helper(root, curr_level, leaf_levels):
        #     if root:
        #         curr_level += 1
        #         if not root.left and not root.right:
        #             leaf_levels.append(curr_level)
        #         helper(root.left, curr_level, leaf_levels)
        #         helper(root.right, curr_level, leaf_levels)
            
        # leaf_levels = []
        # helper(root, 0, leaf_levels)
        # print(leaf_levels)

        # for i in range(len(leaf_levels) - 1):
        #     if leaf_levels[i] - leaf_levels[i + 1] > 1 or leaf_levels[i] - leaf_levels[i + 1] < -1:
        #         return False
        # return True



t1 = TreeNode(3, 
             TreeNode(9), 
             TreeNode(20, 
                      TreeNode(15),
                      TreeNode(17)))
t2 = TreeNode(1, 
             TreeNode(2, 
                      TreeNode(3), 
                      TreeNode(3, 
                               TreeNode(4), 
                               TreeNode(4))), 
             TreeNode(2))

testCases = [t1, t2]
s = Solution()
for t in testCases:
    print(s.isBalanced(t))
