class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = [-1] * 26
        upper = [-1] * 26
        for i in range(len(word)):
            ch = word[i]
            if 'a' <= ch <= 'z':
                lower[ord(ch) - ord('a')] = i
            else:
                if upper[ord(ch) - ord('A')] == -1:
                    upper[ord(ch) - ord('A')] = i
        count = 0
        for i in range(26):
            if lower[i] != -1 and upper[i] != -1 and lower[i] < upper[i]:
                count += 1
        return count
        