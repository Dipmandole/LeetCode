class Solution(object):
    def numberOfSubstrings(self, s):

        left = 0
        right = 0
        n = len(s)

        # count[0] = 'a', count[1] = 'b', count[2] = 'c'
        count = [0] * 3

        ans = 0

        while right < n:

            # Add current character
            count[ord(s[right]) - ord('a')] += 1

            # Shrink window while it contains a, b, and c
            while count[0] > 0 and count[1] > 0 and count[2] > 0:

                ans += (n - right)

                # Remove left character
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            right += 1

        return ans
        """
        :type s: str
        :rtype: int
        """
        