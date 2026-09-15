class Solution(object):
    def search(self, nums, target):
        st = 0
        end = len(nums) -1
        while st <= end:
            mid = st + (end - st)/2
            if nums[mid] == target:
                return mid

            if nums[st] <= nums[mid]: #left sorted
                if nums[st] <= target and target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else: #right Sorted
                if nums[mid] <= target and target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1
        return -1
