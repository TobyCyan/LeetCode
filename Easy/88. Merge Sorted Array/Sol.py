class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        total = m + n - 1
        while j >= 0:
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[total] = nums2[j]
                j -= 1
            else:
                nums1[total] = nums1[i]
                i -= 1
            total -= 1