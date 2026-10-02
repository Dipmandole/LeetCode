class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        bestBuy = prices[0]
        for i in range(len(prices)):
            if prices[i] > bestBuy:
                maxProfit = max(maxProfit, prices[i] - bestBuy)
            bestBuy = min(bestBuy,prices[i])
        return maxProfit
        
        """
        :type prices: List[int]
        :rtype: int
        """
        