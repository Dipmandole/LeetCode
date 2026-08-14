class Solution(object):
    def maximumLengthSubstring(self, s):
        freq = [0] * 26
        left = 0
        maxLen = 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('a')] += 1
            while freq[ord(s[right]) - ord('a')] >2:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen 

        """
        :type s: str
        :rtype: int
        """
        