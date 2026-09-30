class Solution(object):
    def majorityElement(self, nums):
        # Moore's Voting Algorithm
        n = len(nums)
        freq = 0
        ans = 0
        for i in range(n):
            if freq == 0:
                ans = nums[i]
            if ans == nums[i]:
                freq += 1
            else:
                freq -= 1
        return ans

        '''
            if freq == 0:
                ans = nums[i]

            if ans == nums[i]:
                freq += 1
            else:
                freq -= 1

        return ans   '''
        """
        :type nums: List[int]
        :rtype: int
        """
        