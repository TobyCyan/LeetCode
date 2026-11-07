class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
    
        def inBounds(r, c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def dfs(r, c):
            if not inBounds(r, c) or grid[r][c] == 0 or visited[r][c]:
                return 0
            
            visited[r][c] = True
            top = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return 1 + top + down + left + right
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                
                area = dfs(i, j)
                maxArea = max(maxArea, area)
        return maxArea
