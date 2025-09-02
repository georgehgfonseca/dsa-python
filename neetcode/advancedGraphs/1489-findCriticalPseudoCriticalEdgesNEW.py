class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # for each edge, simulate its removal, then check the mst
        # track the edge usage to identify critical and pseudo edges
        criticalEdges = []
        pseudoCriticalEdges = []
        edgeIdx = {(u, v, w): i for i, (u, v, w) in enumerate(edges)}
        edges.sort(key=lambda x: x[2])

        def kruskal(edges, forbiddenEdge, enforcedEdge = None):
            parent = [node for node in range(n)]
            mst = set()
            cost = 0
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                parent[find(i)] = find(j)

            if enforcedEdge:
                (u, v, w) = enforcedEdge
                mst.add(edgeIdx[(u, v, w)])
                cost += w
                union(u, v)
            
            for (u, v, w) in edges:
                if len(mst) == n - 1:
                    break
                if forbiddenEdge == (u, v, w):
                    continue
                if find(u) != find(v):
                    mst.add(edgeIdx[(u, v, w)])
                    cost += w
                    union(u, v)
            if len(mst) != n - 1:
                cost = float("inf")
            return mst, cost

        mst, optimalCost = kruskal(edges, None, None)
        
        for (u, v, w) in edges:
            # run kruskal simulating its removal
            mst, cost = kruskal(edges, (u, v, w), None)
            if cost > optimalCost:
                criticalEdges.append(edgeIdx[(u, v, w)])
                continue
            
            # run kruskal enforcing its addition
            mst, enforcedCost = kruskal(edges, None, (u, v, w))
            if enforcedCost == cost:
                pseudoCriticalEdges.append(edgeIdx[(u, v, w)])

        
        return [criticalEdges, pseudoCriticalEdges] 

