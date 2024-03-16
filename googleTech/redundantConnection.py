from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for (n1, n2) in edges:
            if not union(n1, n2):
                return [n1, n2]


testCases = [
    [[7,8],[2,6],[2,8],[1,4],[9,10],[1,7],[3,9],[6,9],[3,5],[3,10]],
    [[1,5],[3,4],[3,5],[4,5],[2,4]],
    [[1,2],[1,3],[2,3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
]

s = Solution()
for t in testCases:
    print(s.findRedundantConnection(t))