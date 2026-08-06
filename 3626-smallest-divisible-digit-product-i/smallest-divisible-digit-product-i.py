class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            num = n
            product = 1
            while num > 0:
                dig = num % 10
                product *= dig
                num//=10
            if product % t == 0:
                return n
            n += 1

                


        """
        :type n: int
        :type t: int
        :rtype: int
        """
        