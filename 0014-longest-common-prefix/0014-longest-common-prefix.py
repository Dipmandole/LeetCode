class Solution (object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the first string as a starting reference
        prefix = strs[0]

        for s in strs[1:]:
            # Shorten the prefix until the current string starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix