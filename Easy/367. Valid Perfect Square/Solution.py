class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        
        l, r, ans = 0, num, 0

        while l <= r:
            mid = l + (r - l) // 2
            check = mid * mid
            if check == num:
                return True
            elif check > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
    