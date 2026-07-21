class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        n = len(s)
        ones = 0
        maxsum = 0
        prev_run = -1
        i = 0
        
        while i<n:
            if s[i] == '1':
                ones += 1
                i += 1
            else:
                curr = 0
                while i < n and s[i] == '0':
                    curr += 1
                    i += 1
                if prev_run > 0:
                    maxsum = max(maxsum, prev_run + curr)
                prev_run = curr
        return ones + maxsum
        """
        :type s: str
        :rtype: int
        """
        