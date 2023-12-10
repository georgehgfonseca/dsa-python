from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = float("-inf")
        def dfs(root):
            if root:
                left = dfs(root.left) if root.left else 0
                right = dfs(root.right) if root.right else 0
                curr = root.val
                left_curr = left + root.val
                right_curr = right + root.val
                left_curr_right = left + root.val + right
                node_max = max(curr, left_curr, right_curr, left_curr_right)
                self.max_sum = max(self.max_sum, node_max)
                # chat gpt fixed this bug
                return max(root.val, root.val + max(left, right))
                # return node_max
            return float("-inf")
        
        if not root.left and not root.right:
            return root.val

        dfs(root)
        return self.max_sum
        # return self.max_sum
        # # create a graph from tree
        # graph = {}

        # def dfs(root):
        #     if root:
        #         if root not in graph:
        #             graph[root] = set()
        #         if root.left:
        #             graph[root].add(root.left)
        #             if root.left not in graph:
        #                 graph[root.left] = set()
        #             graph[root.left].add(root)
        #             dfs(root.left)
        #         if root.right:
        #             graph[root].add(root.right)
        #             if root.right not in graph:
        #                 graph[root.right] = set()
        #             graph[root.right].add(root)
        #             dfs(root.right)

        # dfs(root)

        # # calculate the distances between each node to each node and get the max
        # self.max = float("-inf")
        # def dijkstra(s):
        #     dist = {node: node.val for node in graph}



        # for node in graph:
        #     dijkstra(node)



tree0 = TreeNode(-10, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15),
                          TreeNode(7)))
tree1 = TreeNode(-2, 
                 TreeNode(-1), 
                 None) 
tree2 = TreeNode(3, 
                 TreeNode(1,
                          TreeNode(0),
                          TreeNode(2)), 
                 TreeNode(5, 
                          TreeNode(4),
                          TreeNode(6)))
tree3 = TreeNode(2, 
                 TreeNode(1), 
                 TreeNode(3))
tree4 = TreeNode(2, 
                 TreeNode(2), 
                 TreeNode(2))
tree5 = TreeNode(5, 
                 TreeNode(1), 
                 TreeNode(4, 
                          TreeNode(3), 
                          TreeNode(6)))

testCases = [
    tree0, 
    tree1, 
    tree2, 
    tree3, 
    tree4, 
    tree5, 
]

s = Solution()
for t in testCases:
    print(s.maxPathSum(t))
