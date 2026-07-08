class Solution(object):
    def __init__(self):
        self.mod = 1000000007

    def sumAndMultiply(self, s, queries):
        n = len(s)

        presum = [0] * (n + 1)                
        coval = [0] * (n + 1)
        count = [0] * (n + 1)
        pow10 = [0] * (n + 1)

        for i in range(1, n + 1):
            num = int(s[i - 1])
            presum[i] = (presum[i - 1] + num) % self.mod

            if num == 0:
                coval[i] = coval[i - 1]
                count[i] = count[i - 1]
            else:
                coval[i] = (coval[i - 1] * 10 + num) % self.mod
                count[i] = count[i - 1] + 1
        pow10[0] = 1
        for i in range(1, n+1):
            pow10[i] = (pow10[i - 1] * 10) % self.mod
        
        ans = []
        for left, right in queries:
            digit_sum = (
                presum[right + 1] - presum[left] + self.mod
            ) % self.mod

            left_part = coval[left]
            right_part = coval[right + 1]

            diff = count[right + 1] - count[left]
            power = pow10[diff]

            concat = (
                right_part - 
                (left_part * power) % self.mod +
                self.mod
            ) % self.mod
            ans.append((concat * digit_sum) % self.mod)
        return ans





        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        