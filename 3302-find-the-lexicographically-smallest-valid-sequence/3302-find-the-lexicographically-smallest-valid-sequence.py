class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)
        # last[i] = index in word1 where word2[i] can be matched
        last = [-1] * m
        word2Index = m - 1

        for word1Index in range(n - 1, -1, -1):
            if word2Index < 0:
                break
            
            if word1[word1Index] == word2[word2Index]:
                last[word2Index] = word1Index
                word2Index -= 1
        
        result = [0] * m
        usedChange = False
        word2Index = 0

        for word1Index in range(n):
            if word2Index >= m:
                break
            currentChar = word1[word1Index]
            requiredChar = word2[word2Index]

            charactersMatch = currentChar == requiredChar

            canUseChange = (
                not usedChange
                and (
                    word2Index == m - 1
                    or word1Index < last[word2Index + 1]
                )
            )

            if charactersMatch or canUseChange:
                result[word2Index] = word1Index
                if not charactersMatch:
                    usedChange = True
                word2Index += 1
        if word2Index < m:
            return []
        return result
        
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        