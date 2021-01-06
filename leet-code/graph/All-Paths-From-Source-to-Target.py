"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from collections import defaultdict

class Solution:
    
    def backtrack(self,source, des, parent):
        # return list contains path
        p = des
        path = []
        while source != p:
            path.append(p)
            p = parent[p]
        path.append(p)
        return path[::-1]

    def allPathsSourceTarget(self, graph):
        ans = []
        parent = {}
        target = len(graph) - 1

        def dfs(node):          
            if node == target:  
                ans.append(self.backtrack(0,target,parent))
                return
            for neighbour in graph[node]:
                    parent[neighbour] = node
                    dfs(neighbour)
                    

        dfs(0)

        return ans
        
        
s = Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
print(s)








