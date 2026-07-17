class Solution(object):
    def gcdValues(self, nums, queries):
        
        m = max(nums)

        count = [0] * (m + 1)

        for num in nums:
            count[num] += 1
        
        gcdPairs = [0] * (m + 1)

        for i in range(1, m + 1):
            total = 0

            for j in range(i, m + 1, i):
                total += count[j]

            gcdPairs[i] = total * (total - 1) // 2

        for i in range(m, 0, -1):
            for j in range(2 * i, m + 1, i):
                gcdPairs[i] -= gcdPairs[j]
        
        presum = [0] * (m + 1)

        for i in range(1, m + 1):
            presum[i] = presum[i - 1] + gcdPairs[i]

        ans = []

        for q in queries:
            k = q + 1

            left = 1
            right = m

            while left < right:
                mid = left + (right - left) // 2
                if presum[mid] >= k:
                    right = mid
                else:
                    left = mid + 1
            ans.append(left)
        return ans
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        