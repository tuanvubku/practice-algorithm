"""
https://leetcode.com/problems/triangle/
Des: 
"""
from copy import deepcopy

class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = deepcopy(triangle[len(triangle) - 1])
 
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            
            for j in range(len(row)):
                dp[j] = row[j] + min(dp[j], dp[j+1])

        return dp[0]
    
s = Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(s)
