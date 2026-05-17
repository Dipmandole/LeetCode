class Solution(object):
    def fourSum(self, nums, target):
        n= len(nums)
        res = []
        nums.sort()

        for a in range (n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range (a+1, n):
                if b > (a+1) and nums[b] == nums[b-1]:
                    continue
                c, d = b + 1, n-1
                while c < d:
                    quad = [nums[a], nums[b], nums[c] ,nums[d]]
                    q_sum = sum(quad)
                    if q_sum > target : d -= 1
                    elif q_sum < target: c += 1
                    else:
                        res.append(quad)
                        while c < d and nums[c] == quad[2]: c += 1
                        while c < d and nums[d] == quad[3]: d -= 1
        return res

        