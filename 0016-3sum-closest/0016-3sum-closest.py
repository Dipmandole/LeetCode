class Solution(object):
    def threeSumClosest(self, nums, target):

        cs = float('inf')

        nums.sort()

        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                ts = nums[i] + nums[l] + nums[r]

                # Update closest sum
                if abs(cs - target) > abs(ts - target):
                    cs = ts

                # Move pointers
                if ts > target:
                    r -= 1

                elif ts < target:
                    l += 1

                else:
                    return ts

        return cs