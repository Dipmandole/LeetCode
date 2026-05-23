class Solution(object):
    def check(self, nums):
        n = len(nums)
        point = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                point += 1

        return point <= 1
        