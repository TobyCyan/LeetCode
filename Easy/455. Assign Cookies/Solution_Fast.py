class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        m, n = len(g), len(s)
        if n == 0:
            return 0

        # O(mlogm + nlogn) for sorting
        sorted_g = sorted(g)
        sorted_s = sorted(s)

        # O(max(m, n)) or O(m + n) for the two-pointer traversal
        child, cookie = 0, 0
        while child < m and cookie < n:
            if sorted_g[child] <= sorted_s[cookie]:
                child += 1
            cookie += 1

        return child