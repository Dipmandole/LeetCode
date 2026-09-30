class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        ans = nums[0]
        freq = 1
        for i in range(n):
            if nums[i] == nums[i - 1]:
                freq += 1
            else:
                freq = 1
                ans = nums[i]
            if freq > n / 2:
                return ans
            
        return ans


        # Moore's Voting Algorithm
        '''n = len(nums)
        freq = 0
        ans  = 0
        for i in range(len(nums)):

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
        