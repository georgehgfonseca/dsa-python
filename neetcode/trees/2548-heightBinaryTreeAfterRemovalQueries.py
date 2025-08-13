from typing import Dict, Tuple, Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        nodeDepth = dict()
        nodeHeight = dict()

        def dfs(root, depth):
            if not root:
                return 0
            
            nodeDepth[root.val] = depth
            currHeight = max(1 + dfs(root.left, depth + 1), 1 + dfs(root.right, depth + 1))
            nodeHeight[root.val] = currHeight - 1
            return currHeight
        
        dfs(root, 0)

        depthNodesHeights: Dict[int, Tuple[int, int]] = defaultdict(list)
        for node in nodeDepth:
            depth = nodeDepth[node]
            height = nodeHeight[node]
            depthNodesHeights[depth].append((node, height))
        
        # sort nodes in depthNodesHeights by height
        for depth in depthNodesHeights:
            depthNodesHeights[depth].sort(key= lambda x: x[1], reverse= True)

        res = []
        for query in queries:
            depth = nodeDepth[query]
            isOnlyNodeInDepth = len(depthNodesHeights[depth]) == 1
            if isOnlyNodeInDepth:
                res.append(depth - 1)
            else:
                # cousing nodes (including itself) are sorted by height
                for (cousingNode, height) in depthNodesHeights[depth]:
                    if cousingNode == query:
                        continue
                    break
                res.append(depth + height)
            
        return res


    def treeQueries3(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        nodeDepth = dict()
        depthNodes = defaultdict(set)
        nodeHeight = dict()
        heightNodes = defaultdict(set)

        def dfs(root, depth):
            if not root:
                return 0
            
            nodeDepth[root.val] = depth
            depthNodes[depth].add(root.val)
            currHeight = max(1 + dfs(root.left, depth + 1), 1 + dfs(root.right, depth + 1))
            nodeHeight[root.val] = currHeight - 1
            heightNodes[currHeight - 1].add(root.val)
            return currHeight
        
        dfs(root, 0)

        # TODO: at each depth, keep only the 2 nodes with largest height / sort by height
        res = []
        for query in queries:
            depth = nodeDepth[query]
            isOnlyNodeInDepth = len(depthNodes[depth]) == 1
            if isOnlyNodeInDepth:
                res.append(depth - 1)
            else:
                # get cousin with max height
                maxHeight = -1
                for cousinNode in depthNodes[depth]:
                    if cousinNode != query and nodeHeight[cousinNode] > maxHeight:
                        maxHeight = nodeHeight[cousinNode]
                res.append(depth + maxHeight)
            
        return res

    def treeQueries2(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        def dfs(root, query):
            if not root or root.val == query:
                return 0

            return max(1 + dfs(root.left, query), 1 + dfs(root.right, query))
            
        cache = {}
        res = []
        for query in queries:
            if query in cache:
                res.append(cache[query])
                continue

            depth = dfs(root, query) - 1
            cache[query] = depth
            res.append(depth)

        return res
