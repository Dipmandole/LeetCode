#Approach-1 (Using simple resurion + memoization)
class Solution(object):
    def stoneGameIII(self, stoneValue):
        
        n = len(stoneValue)
        dp = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = stoneValue[i] - solve(i + 1)
            if i + 1 < n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - solve(i + 2))
            
            if i + 2 < n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(i + 3))
            return dp[i]
        
        diff = solve(0)
        if diff > 0:
            return 'Alice'
        elif diff < 0:
            return 'Bob'
        else:
            return 'Tie'

        """
        :type stoneValue: List[int]
        :rtype: str
        """
        