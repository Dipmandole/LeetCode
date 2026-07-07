class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)
        ans = 0
        digit_sum = 0
        for ch in s:
            digit = int(ch)
            if digit != 0:
                digit_sum += digit
                ans = ans * 10 + digit
        return digit_sum * ans
        """
        :type n: int
        :rtype: int
        """
        x