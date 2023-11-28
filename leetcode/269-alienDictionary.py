from typing import List

# premium problem available in https://leetcode.ca/all/269.html
class Solution:
    def alienDictionary(self, alienWords: List[List[str]]) -> str:
        # create a graph of letter precedences
        graph = {}
        for word in alienWords:
            if len(word) == 1:
                if word[0] not in graph:
                    graph[word[0]] = {}

            for i in range(len(word) - 1):
                if word[i] not in graph:
                    graph[word[i]] = {}
                graph[word[i]][word[i + 1]] = 1

        # run a topological sort algorithm to find the order in the alien alphabet
        self.order = ""
        discovered = {node: 0 for node in graph}
        def dfs(node, discovered):
            discovered[node] = 1
            for neighbor in graph[node]:
                if discovered[neighbor] == 0:
                    dfs(neighbor, discovered)
            self.order = node + self.order

        # run dfs for each undiscovered node
        for node in graph:
            if discovered[node] == 0:
                dfs(node, discovered)
        return self.order


t1 = ["wrt",
      "wrf",
      "er",
      "ett",
      "rftt"]
t2 = ["z",
      "x"]
t3 = ["z",
      "x",
      "z"]
testCases = [t1, t2, t3]
s = Solution()
for t in testCases:
    print(s.alienDictionary(t))
