class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]
                if a + b == target:
                    return [i,j]
        

        """
         n = len(nums)

        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]

                if a + b == target:
                    return [i, j]
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        