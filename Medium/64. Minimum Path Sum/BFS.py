from typing import List
from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        class State:
            def __init__(self, r, c, sum):
                self.r = r
                self.c = c
                self.sum = sum
        
        ROWS, COLS = len(grid), len(grid[0])
        def isValid(r, c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS
        
        DIRECTIONS = [
            (1, 0),
            (0, 1)
        ]

        bestSum = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        bestSum[0][0] = grid[0][0]
        
        q = deque()
        q.append(State(0, 0, grid[0][0]))

        while q:
            curr = q.popleft()
            r, c, s = curr.r, curr.c, curr.sum

            if s > bestSum[r][c]:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                continue
            
            for y, x in DIRECTIONS:
                nR, nC = r + y, c + x
                if not isValid(nR, nC):
                    continue

                nS = s + grid[nR][nC]
                if nS < bestSum[nR][nC]:
                    bestSum[nR][nC] = nS
                    q.append(State(nR, nC, nS))
            
        return bestSum[ROWS - 1][COLS - 1]
