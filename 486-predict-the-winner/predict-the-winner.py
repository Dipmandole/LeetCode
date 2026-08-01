class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        def solve(left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]

            if dp[left][right] != -1:
                return dp[left][right]
            
            take_left = nums[left] + min(solve(left + 2, right),
            solve(left + 1, right - 1))

            take_right = nums[right] + min(solve(left, right - 2),
            solve(left + 1, right - 1))

            dp[left][right] = max(take_left, take_right)
            return dp[left][right]
        total = sum(nums)

        player1 = solve(0, n - 1)
        player2 = total - player1

        return player1 >= player2


        """
        :type nums: List[int]
        :rtype: bool
        """
        