class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        count = 0

        if n <= 8:
            count = n
        elif n <= 16:
            count = 8 + (n - 8) * 2
        elif n <= 24:
            count = 24 + (n - 16) * 3
        else:
            count = 48 + (n - 24) * 4
        return count
        """
        :type word: str
        :rtype: int
        """
        