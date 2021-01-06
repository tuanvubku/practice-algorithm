class Solution:
    def numIslands(self, grid) -> int:
        
        def dfs(grid, seen, row_i, col_j):
            if row_i < 0 or col_j < 0 or row_i >= row or col_j >= col or seen[row_i][col_j] == True or grid[row_i][col_j] == "0":
                return False
            seen[row_i][col_j] = True
            dfs(grid, seen, row_i, col_j + 1)
            dfs(grid, seen, row_i, col_j - 1)
            dfs(grid, seen, row_i + 1, col_j)
            dfs(grid, seen, row_i - 1, col_j)
            return True
        
        row = len(grid)
        col = len(grid[0])
        
        count = 0
        seen = [[False for x in range(col)] for y in range(row)]
        
        for i in range(row):
            for j in range(col):
                isIsland = dfs(grid, seen, i, j)
                if isIsland:
                    count += 1
                
        return count

s = Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])