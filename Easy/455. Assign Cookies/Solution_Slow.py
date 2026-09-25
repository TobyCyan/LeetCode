class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        m, n = len(g), len(s)
        if n == 0:
            return 0
        
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        j_start, count = 0, 0
        # O(mn) + O(mlogm) + O(nlogn)
        for i in range(m):
            j = j_start
            while j < n:
                if sorted_s[j] >= sorted_g[i]:
                    count += 1
                    j_start = j + 1
                    break
                j += 1

        return count