class Solution(object):
    def maxProduct(self, nums):
        curr_max = nums[0]
        n = len(nums)
        result = 0
        for i in range(1,n):
            result = max(result,(nums[i] - 1) * (curr_max - 1))
            curr_max = max(curr_max, nums[i])
            i += 1
        return result

        """
        :type nums: List[int]
        :rtype: int
        """
        