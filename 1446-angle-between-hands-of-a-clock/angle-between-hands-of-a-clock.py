class Solution(object):
    def angleClock(self, hour, minutes):
        hour_degree = (hour % 12) * 30 + 0.5 * minutes
        minute_degree = minutes * 6
        diff = abs(hour_degree - minute_degree)
        return min(diff, 360 - diff)
        
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        