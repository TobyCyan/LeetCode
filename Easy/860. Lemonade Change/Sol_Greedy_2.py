class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {5 : 0, 10: 0, 20: 0}
        
        # O(n)
        for bill in bills:
            change[bill] += 1
            # $10 -> Change for $5
            # $20 -> Change for $10 $5, or $5 * 3
            # If cannot satisfy, return False
            if bill == 5:
                continue
            elif bill == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
            else:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True