#Frequency Count (Optimal) O(n)
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        n = len(arr)
        count = [0] * (n + 1)
        for num in arr:
            count[min(num, n)] += 1
        ans = 1

        for i in range(2,n+1):
            nxt = ans + count[i]
            ans = min(i,nxt)
        return ans
        """
        :type arr: List[int]
        :rtype: int
        """
        