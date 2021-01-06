"""

"""
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        print(graph)
        colors = [0] * numCourses

        for i in range(numCourses):
            if colors[i] == 0:
                if not self.dfs(graph, colors, i):
                    return False
        return True
                

    def dfs(self, graph,colors, node):        
        if colors[node] == -1:
            return False
        colors[node] = -1
        for nei in graph[node]:
            self.dfs(graph,colors,nei)
        colors[node] = 1
        return True
        
s= Solution().canFinish(4, [[1,0],[2,0],[1,3],[2,1]])
print(s)

        
        
        