class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        val = items
        bonus = [0] * n

        for i in range(n):
            factor_i = items[i][0]
            for j in range(n):
                if i != j:
                    factor_j = items[j][0]
                    if factor_j % factor_i == 0:
                        bonus[i] +=1
        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            value_f = 1 + bonus[i]
            value_e = 1
            
            new_dp = dp[:]

            for b in range(price, budget + 1):
                new_dp[b] = max(new_dp[b],dp[b - price] + value_f)

                new_dp[b] = max(new_dp[b], new_dp[b - price] + value_e)
            dp = new_dp
        return max(dp)
        