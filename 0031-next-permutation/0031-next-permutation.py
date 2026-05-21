class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """

        ind = -1
        n = len(nums)

        # Step 1: Find breakpoint
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If no breakpoint, reverse whole array
        if ind == -1:
            nums.reverse()
            return

        # Step 3: Find next greater element and swap
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 4: Reverse the remaining part
        nums[ind + 1:] = reversed(nums[ind + 1:])