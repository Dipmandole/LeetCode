class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        result = []
        for i in range(1,len(nums)):
            for j in range(nums[i-1] + 1, nums[i]):
                result.append(j)
        return result
            
                

        