class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp = [0] * n
        comp[0] = 0

        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = i
        ans = []
        for node1, node2 in queries:
            if comp[node1] == comp[node2]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        