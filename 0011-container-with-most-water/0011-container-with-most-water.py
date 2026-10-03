class Solution(object):
    def maxArea(self, height):
        maxAns = 0
        lp = 0
        rp = len(height) - 1
        while lp < rp:
            weight = rp - lp
            wh = min(height[lp], height[rp])
            area = weight * wh
            maxAns = max(maxAns, area)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return maxAns
