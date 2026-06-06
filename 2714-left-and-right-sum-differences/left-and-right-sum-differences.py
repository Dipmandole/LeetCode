class Solution(object):
    def leftRightDifference(self, nums):
        rightsum = 0
        ans = [0] * len(nums)
        for num in nums:
            rightsum += num
        leftsum = 0

        for i in range(len(nums)):
            rightsum -= nums[i]
            ans[i] = abs(rightsum - leftsum)
            leftsum += nums[i]
        return ans