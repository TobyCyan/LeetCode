class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def isBorderCell(r, c):
            return r == 0 or r == m - 1 or c == 0 or c == n - 1
        
        def inBounds(r, c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def dfs(r, c):
            if not inBounds(r, c):
                return False
            
            if grid[r][c] == 1 or visited[r][c]:
                return True
            
            visited[r][c] = True

            down = dfs(r - 1, c)
            up = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            return not isBorderCell(r, c) and up and down and left and right
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or visited[i][j]:
                    continue
                
                isClosedIsland = dfs(i, j)
                if isClosedIsland:
                    count += 1
        
        return count
