class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumOdd = n * (2 * 1 + (n - 1) * 2) // 2 #Odd Number
        sumEven = n * (2 * 2 + (n - 1) * 2) // 2 #Even Number
        return self.gcd(sumOdd,sumEven)
    
    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

        
        """
        :type n: int
        :rtype: int
        """
        