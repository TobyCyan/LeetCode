class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])

        # O(m)
        def findColPeak(c: int):
            maxR = 0
            for r in range(m):
                if mat[r][c] > mat[maxR][c]:
                    maxR = r
            return maxR, c
        
        def valid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def leftPeak(r, c):
            left = c - 1
            return valid(r, left) and mat[r][left] > mat[r][c]
        
        def colPeak(r, c):
            curr = mat[r][c]
            top = not valid(r - 1, c) or mat[r - 1][c] < curr
            bottom = not valid(r + 1, c) or mat[r + 1][c] < curr
            return top and bottom
        
        def rowPeak(r, c):
            curr = mat[r][c]
            left = not valid(r, c - 1) or mat[r][c - 1] < curr
            right = not valid(r, c + 1) or mat[r][c + 1] < curr
            return left and right

        # Binary search over columns -> O(log n)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = findColPeak(mid)
            if rowPeak(row, col):
                return [row, col]

            if leftPeak(row, col):
                r = mid - 1
            else:
                l = mid + 1