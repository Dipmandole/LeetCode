class Solution(object):
    def sequentialDigits(self, low, high):
        s = '123456789'
        min_len = len(str(low))
        max_len = len(str(high))
        ans = []

        for length in range(min_len, max_len + 1):
            for start in range(0, 10 - length):
                substr = s[start:start + length]
                num = int(substr)
                if low <= num <= high:
                    ans.append(num)
        return ans
        
        
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        