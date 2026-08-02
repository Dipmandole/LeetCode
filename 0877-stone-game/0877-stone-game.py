class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]

        def maxDiff(left, right):
            if left == right:
                return piles[left]
            if dp[left][right] != -1:
                return dp[left][right]
            
            take_left = piles[left] - maxDiff(left + 1, right)
            take_right = piles[right] - maxDiff(left, right - 1)
            dp[left][right] = max(take_left, take_right)
            return dp[left][right]

        return maxDiff(0, n - 1) > 0
        """
        :type piles: List[int]
        :rtype: bool
        """
        