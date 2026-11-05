from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def inBounds(i, j):
            return i >= 0 and i < m and j >= 0 and j < n
        
        def dfs(i, j):
            if not inBounds(i, j) or grid[i][j] == "0":
                return
            
            if visited[i][j]:
                return
            
            visited[i][j] = True

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count