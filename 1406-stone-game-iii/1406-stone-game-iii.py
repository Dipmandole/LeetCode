#Approach-2 (Converting approach-1 to Bottom Up)
class Solution(object):
    def stoneGameIII(self, stoneValue):
        
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]

            if i + 1 < n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
            
            if i + 2 < n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])
    
        
        diff = dp[0]
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
        