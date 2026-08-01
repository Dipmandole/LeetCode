class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        def maxDiff(left, right):
            if left == right:
                return nums[left]
            
            if dp[left][right] != -1:
                return dp[left][right]
            
            take_left = nums[left] - maxDiff(left + 1, right)
            take_right = nums[right] - maxDiff(left, right - 1)


            dp[left][right] = max(take_left, take_right)
            return dp[left][right]
        return maxDiff(0, n - 1) >= 0


        """
        :type nums: List[int]
        :rtype: bool
        """
        