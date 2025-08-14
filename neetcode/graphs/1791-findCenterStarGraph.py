class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for source, sink in edges:
            graph[source].add(sink)
            graph[sink].add(source)
            if len(graph[source]) >= 2:
                return source
            if len(graph[sink]) >= 2:
                return sink