class Solution(object):
    def findGCD(self, nums):
        maximum = max(nums)
        minimum = min(nums)
        return self.gcd(maximum,minimum)
    
    def gcd(self,a,b):
        while b != 0:
            a,b = b, a % b
        return a
        """
        :type nums: List[int]
        :rtype: int
        """
        