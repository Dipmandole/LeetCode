class Solution(object):
    def numberOfSpecialChars(self, word):
        f1 = [0] * 26
        f2 = [0] * 26

        for ch in word:
            if 'a' <= ch <= 'z':
                f1[ord(ch) - ord('a')] += 1
            else:
                f2[ord(ch) - ord('A')] += 1
        
        count = 0

        for i in range(26):
            if f1[i] > 0 and f2[i] > 0:
                count += 1
        return count
        