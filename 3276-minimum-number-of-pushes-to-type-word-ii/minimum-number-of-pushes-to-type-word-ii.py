class Solution(object):
    def minimumPushes(self, word):
        freq = [0] * 26
        
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        freq.sort()

        ans = 0
        idx = 0

        for i in range(25,-1,-1):
            if freq[i] == 0:
                continue
            ans += freq[i] * ((idx // 8) + 1)
            idx += 1
        return ans
