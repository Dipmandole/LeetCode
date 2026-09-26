class Solution(object):
    def maxSubArray(self, nums):
        #Kadane's Algorithm

        maxSum = float('-inf')
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum
        """
        :type nums: List[int]
        :rtype: int
        """
        