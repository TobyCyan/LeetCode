class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # 2 pointers, keep moving right and keep track of the highest count until see a 0.
        # Attempt to delete the 0, if no more deletion, reset the left pointer to the last deleted position + 1 and delete the new 0.
        is_deleted = False
        highest = 0
        last_deletion = 0
        l = 0
        for r in range(len(nums)):
            is_one = nums[r]
            if is_one:
                curr = r - l + (0 if is_deleted else 1)
                highest = max(highest, curr)
                continue
            
            if not is_deleted:
                is_deleted = True
            else:
                l = last_deletion + 1
            
            # When we see a 0, either we delete this and proceed,
            # or we delete and move the left pointer if this is not the first time deleting a 0.
            last_deletion = r
        
        return highest - (0 if is_deleted else 1)