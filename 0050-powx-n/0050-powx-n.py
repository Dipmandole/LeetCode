class Solution(object):
    def myPow(self, x, n):
        negative = False

        if n < 0:
            negative = True
            n = -n

        ans = 1.0

        while n > 0:

            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        if negative:
            ans = 1.0 / ans

        return ans
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        