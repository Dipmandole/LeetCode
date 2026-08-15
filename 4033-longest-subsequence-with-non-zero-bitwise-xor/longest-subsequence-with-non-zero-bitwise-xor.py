class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        xr = 0
        allzero = True

        for x in nums:
            xr ^= x
            if x != 0:
                allzero = False

        if xr != 0:
            return n

        if allzero:
            return 0

        return n - 1