class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        M = 200
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [row[:] for row in dp]
            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    val = dp[g1][g2]
                    if val == 0:
                        continue
                    
                    ng1 = num if g1 == 0 else gcd(g1, num)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + val) % MOD
                    
                    ng2 = num if g2 == 0 else gcd(g2, num)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + val) % MOD
            
            dp = new_dp
        
        answer = 0
        for g in range(1, M + 1):
            answer = (answer + dp[g][g]) % MOD
        
        return answer