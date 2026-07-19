class Solution(object):
    def smallestSubsequence(self, s):
        n = len(s)
        last = [0] * 26
        for i in range(n):
            last[ord(s[i]) - ord('a')] = i
        
        stack = []
        visited = set()

        for i in range(n):
            ch = s[i]

            if ch in visited:
                continue
            while stack:
                prev = s[stack[-1]]
                if prev > ch and last[ord(prev) - ord('a')] > i:
                    visited.remove(prev)
                    stack.pop()
                else:
                    break
            stack.append(i)
            visited.add(ch)
        ans = []
        for idx in stack:
            ans.append(s[idx])
        return "".join(ans)

        """
        :type s: str
        :rtype: str
        """
        