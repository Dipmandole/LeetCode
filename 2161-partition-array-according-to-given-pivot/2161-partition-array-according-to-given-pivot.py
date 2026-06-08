class Solution(object):
    def pivotArray(self, nums, pivot):
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n-1

        # left arr inserted
        for i in range(n):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left +=1
        # right arr inserted
        for i in range(n-1,-1,-1):
            if nums[i] > pivot:
                ans[right] = nums[i]
                right -=1
        # remaning element of pivot only
        while left <= right:
            ans[left] = pivot
            left +=1
        return ans
        