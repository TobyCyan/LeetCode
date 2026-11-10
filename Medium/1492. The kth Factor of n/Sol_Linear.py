class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def isFactor(n, i):
            return n % i == 0
        
        if k == 1:
            return 1
        
        count = 1
        for i in range(2, n):
            if isFactor(n, i):
                count += 1
            
            if count == k:
                return i
        
        if count + 1 == k:
            return n
        
        return -1