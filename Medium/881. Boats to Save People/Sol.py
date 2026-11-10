class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        boats = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                # Ship off both persons
                boats += 1
                l += 1
                r -= 1
            else:
                # One boat for the heavier person
                boats += 1
                r -= 1
        return boats
