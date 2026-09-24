class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        