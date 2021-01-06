class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        def dfs(row_i, col_j):
            if(row_i < 0 or row_i == row or col_j < 0 or col_j == col or seen[row_i][col_j] == True):
                return
            if board[row_i][col_j] == "X":
                return
            if board[row_i][col_j] == "O":
                board[row_i][col_j] = 1
            seen[row_i][col_j] = True
            dfs(row_i + 1, col_j)
            dfs(row_i - 1, col_j)
            dfs(row_i , col_j + 1)
            dfs(row_i , col_j - 1)
        row = len(board)
        col = len(board[0])
        
        seen = [[False for x in range(col)] for y in range(row)]
        
        for i in range(col):
            dfs(0, i)
            dfs(row - 1, i)
            
        for j in range(1,row-1):
            dfs(j,0)
            dfs(j, col - 1)
        
        for a in range(row):
            for b in range(col):
                if board[a][b] == 1:
                    board[a][b] = "O"
                elif board[a][b] == "O":
                    board[a][b] = "X"