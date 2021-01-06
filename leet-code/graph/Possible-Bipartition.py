"""
"""
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = defaultdict(list)
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        colors = [-1] * (N + 1)
        visit = set()
        
        for i in range(1,N+1):
            if i not in visit:
                if self.isBipartition(i,graph,visit,colors) == False:
                    return False
        return True
    
    def isBipartition(self, node, graph, visit,colors):
        
        q = [node]
        colors[node] = 1
        
        
        while q:
            node = q.pop(0)
            visit.add(node)
            
            for neighbour in graph[node]:
                if colors[neighbour] == -1:
                    colors[neighbour] = 1 - colors[node]
                    q.append(neighbour)
                elif colors[neighbour] == colors[node]:
                    return False
                
        return True