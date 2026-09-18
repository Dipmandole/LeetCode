class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        lb = n
        st = 0
        end = n -1
        while st <= end:
            mid = (st + end) // 2
            if nums[mid] >= target:
                lb = mid
                end = mid - 1
            else:
                st = mid + 1
        return lb
