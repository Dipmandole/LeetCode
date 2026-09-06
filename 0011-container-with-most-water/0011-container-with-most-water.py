class Solution(object):
    def maxArea(self, height):
        Left = 0
        Right = len(height) - 1
        maxArea = float("-inf")
        while Left < Right:
            value = min(height[Left], height[Right]) * (Right - Left)
            maxArea = max(maxArea,value)
            if height[Left] < height[Right]:
                Left += 1
            else:
                Right -= 1
        return maxArea