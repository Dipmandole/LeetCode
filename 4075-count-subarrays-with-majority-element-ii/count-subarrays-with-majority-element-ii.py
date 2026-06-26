class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        size = 2 * n + 2
        countAtSum = [0] * size
        cumulativeCount = [0] * size

        idx = n + 1
        countAtSum[idx] = 1
        cumulativeCount[idx] = 1
        ans = 0
        
        for num in nums:
            if num == target:
                idx += 1
            else:
                idx -= 1
            countAtSum[idx] += 1
            ans += cumulativeCount[idx -1]
            cumulativeCount[idx] = (cumulativeCount[idx-1] + countAtSum[idx])
        return ans


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        