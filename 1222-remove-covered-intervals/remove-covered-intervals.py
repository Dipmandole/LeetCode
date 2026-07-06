class Solution(object):
    def removeCoveredIntervals(self, intervals):
        n = len(intervals)
        intervals.sort(key = lambda x : [x[0], -x[1]])
        remove = 0
        prev = 0
        for i in range(1, n):
            start, end = intervals[i]
            pstart, pend = intervals[prev]

            if start >= pstart and end <= pend:
                remove += 1
            else:
                prev = i
        return n - remove
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        