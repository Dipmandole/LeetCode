class Solution(object):
    def largestInteger(self, nums, k):
        count = [0] * 51
        for i in range(len(nums) - k + 1):
            seen = [False] * 51
            for j in range(i, i + k):
                seen[nums[j]] = True
            for num in range(51):
                if seen[num]:
                    count[num] += 1
        for num in range(50, -1, -1):
            if count[num] == 1:
                return num
        return -1
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        