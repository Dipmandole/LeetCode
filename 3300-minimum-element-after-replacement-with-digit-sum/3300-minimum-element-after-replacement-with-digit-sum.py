class Solution(object):
    def minElement(self, nums):
        ans = float('inf') 
        for num in nums:
            digits_sum = self.getDigitSum(num)
            ans = min(ans,digits_sum)
        return ans

    def getDigitSum(self,num):
        total = 0
        while num > 0:
           total += num % 10
           num = num // 10
        return total