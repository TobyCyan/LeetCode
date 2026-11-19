class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {5 : 0, 10: 0, 20: 0}
        price = 5
        
        # O(1)
        def totalChange():
            total = 0
            for k, v in change.items():
                total += k * v
            return total
        
        # O(n)
        for bill in bills:
            expectedChange = bill - price
            total = totalChange()
            if expectedChange > total:
                return False

            change[bill] += 1
            # Start from second highest denomination (A customer who paid 20 won't expect to have 20 back)
            # O(1)
            k = 10
            while expectedChange > 0:
                if k < 5:
                    return False
                
                while change[k] > 0:
                    if k > expectedChange:
                        break
                    expectedChange -= k
                    change[k] -= 1
                k -= 5

        return True