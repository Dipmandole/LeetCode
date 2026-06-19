class Solution(object):
    def largestAltitude(self, gain):
        maxi = 0
        curr = 0

        for g in gain:
            curr += g
            maxi = max(curr, maxi)
        return maxi
        """
        :type gain: List[int]
        :rtype: int
        """
        