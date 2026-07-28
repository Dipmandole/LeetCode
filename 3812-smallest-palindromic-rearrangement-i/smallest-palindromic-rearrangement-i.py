from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        mid = ''
        first = ''
        count = Counter(s)

        for ch in sorted(count):
            if count[ch]%2 == 1:
                if mid != '':
                    return ''
                mid = ch
            first += ch * (count[ch]//2)
        return first + mid + first[::-1]
            
        
        """
        :type s: str
        :rtype: str
        """
        