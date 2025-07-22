from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets to ensure ordering
        tickets.sort()

        # create a graph
        graph = {source: [] for source, sink in tickets}
        for (source, sink) in tickets:
            graph[source].append(sink)

        # dfs
        initial_node = "JFK"
        itinerary = [initial_node]
        def dfs(node):
            if len(itinerary) == len(tickets) + 1:
                return True
            if node not in graph:
                return False
            
            neighbors = list(graph[node])
            for i, neighbor in enumerate(neighbors):
                graph[node].pop(i)
                itinerary.append(neighbor)
                if dfs(neighbor):
                    return True
                
                graph[node].insert(i, neighbor)
                itinerary.pop()
            return False
                
        dfs(initial_node)
        return itinerary


    
s = Solution()
print(s.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]))