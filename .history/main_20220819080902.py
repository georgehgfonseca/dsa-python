from typing import List
import searchSort
from binaryTree import TreeNode
from graph import Graph
from weightedGraph import WeightedGraph
import combinatorics
import strings
import random
import time

# Sandbox for testing
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open = ""
        res = [""]
        for i in range(len(s)):
            print("open:", open)
            if s[i] != "(" and s[i] != ")":
                for r in range(len(res)):
                    res[r] += s[i]
                continue
            if s[i] == "(":
                for r in range(len(res)):
                    res[r] += s[i]
                open += s[i]
            elif s[i] == ")":
                if len(open) == 0:
                    # at least one correction must be made
                    k = 0
                    k_max = len(res)
                    while k < k_max:
                        r = res[k] + ")"
                        k += 1
                        for j in range(len(r) - 1):
                            if r[j] == ")":
                                # create a new answer removing this ')'
                                rNew = r[:j] + r[j + 1 :]
                                # rNew.pop(j)
                                # rNew += ')'
                                res.append(rNew)
                elif open[-1] == "(":
                    # remove open paranthesis
                    open = open[:-1]
                    for r in range(len(res)):
                        res[r] += s[i]
            print("all: ", s[i], res, open)
        return res


# r = "()())()"
r = "(a)())()"
s = Solution()
print(s.removeInvalidParentheses(r))
# j = 4
# rNew = r[:j] + r[j + 1 :] + ")"
# print(rNew)


# Search and Sort algorithms
# array = []
# searchSort.push_in_order(array, 1)
# searchSort.push_in_order(array, 5)
# searchSort.push_in_order(array, 10)
# print(array)
# print(searchSort.binarySearchRec(array, 8))
# array = [6, 7, 3, 8, 9, 2, 1, 4]
# array = [random.randrange(10000 * 10) for i in range(10000)]
# tIni = time.time()
# searchSort.bubble_sort(array)
# searchSort.selection_sort(array)
# searchSort.insertion_sort(array)
# searchSort.merge_sort(array)
# searchSort.quick_sort(array, 0, len(array) - 1)
# print(time.time() - tIni)


# # String algorithms
# s = "araras"
# print(strings.palindrome(s))

# # Tree algorithms
# tree = TreeNode(2)
# tree.addNode(tree, 5)
# tree.addNode(tree, 4)
# tree.addNode(tree, 1)
# tree.addNode(tree, 7)
# print(tree.traversePreorder(tree))
# print(tree.traverseOrder(tree))
# print(tree.traversePostorder(tree))

# # Graph algorithms
# graph = WeightedGraph(6)
# graph.addUndirectedEdge(0, 1, 1)
# graph.addUndirectedEdge(0, 3, 1)
# graph.addUndirectedEdge(3, 2, 1)
# graph.addUndirectedEdge(1, 4, 1)
# graph.addUndirectedEdge(2, 4, 1)
# graph.addUndirectedEdge(1, 5, 1)
# print(graph.adjList)
# print(graph.bfs(0))
# print(graph.dfs(0))
# print(graph.connected())
# print(graph.dijkstra_pq(0, 5))

# # Combiantorics algorithms
# print(combinatorics.findSubsets([1, 2, 3, 4], 2))
# print(combinatorics.allSubsets([1, 2, 3, 4]))
