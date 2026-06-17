class Solution(object):
    def processStr(self, s, k):
        # Forward pass: calculate final string length
        length = 0

        for ch in s:

            if 'a' <= ch <= 'z':
                length += 1

            elif ch == '#':
                length *= 2

            elif ch == '*':
                if length > 0:
                    length -= 1

            # '%' does not change length

        # k is outside final string
        if k >= length:
            return '.'

        # Backward pass
        for i in range(len(s) - 1, -1, -1):

            ch = s[i]

            if ch == '*':

                # Undo deletion
                length += 1

            elif ch == '#':

                # Undo doubling
                length //= 2

                # Map second half to first half
                if k >= length:
                    k -= length

            elif ch == '%':

                # Undo reverse
                k = length - 1 - k

            else:

                # Undo append
                length -= 1

                if length == k:
                    return ch

        return '.'
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        