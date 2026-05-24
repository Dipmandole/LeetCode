class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)

        # Memoization array
        self.jumps = [-1] * n

        # Calculate max jumps from every index
        for i in range(n):
            self.jumps[i] = self.dfs(i, arr, d)

        return max(self.jumps)

    def dfs(self, ind, arr, d):

        # Return cached result
        if self.jumps[ind] != -1:
            return self.jumps[ind]

        # Minimum jump count is 1 (stay at current index)
        self.jumps[ind] = 1

        # Explore left side
        for i in range(ind - 1, max(-1, ind - d - 1), -1):

            # Stop if greater or equal value found
            if arr[i] >= arr[ind]:
                break

            self.jumps[ind] = max(
                self.jumps[ind],
                self.dfs(i, arr, d) + 1
            )

        # Explore right side
        for i in range(ind + 1, min(len(arr), ind + d + 1)):

            # Stop if greater or equal value found
            if arr[i] >= arr[ind]:
                break

            self.jumps[ind] = max(
                self.jumps[ind],
                self.dfs(i, arr, d) + 1
            )

        return self.jumps[ind]