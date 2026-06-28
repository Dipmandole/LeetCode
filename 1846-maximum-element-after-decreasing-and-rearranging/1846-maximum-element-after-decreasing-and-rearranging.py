#Sorting Approach O(log n)
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        n = len(arr)

        if arr[0] != 1:
            arr[0] = 1

        for i in range(1,n):
            if abs(arr[i] - arr[i-1] > 1):
                arr[i] = arr[i-1] + 1
        return arr[-1]
        """
        :type arr: List[int]
        :rtype: int
        """
        