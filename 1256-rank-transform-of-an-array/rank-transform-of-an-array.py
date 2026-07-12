class Solution(object):
    def arrayRankTransform(self, arr):
        n = len(arr)
        if n == 0:
            return []

        temp = []

        for i in range(n):
            temp.append([arr[i], i])
        temp.sort(key = lambda x: x[0])
        ans = [0] * n
        rank = 1
        prev = temp[0][0]
        idx = temp[0][1]
        ans[idx] = 1
        
        for i in range(1, n):
            val = temp[i][0]
            idx = temp[i][1]
            if val != prev:
                rank += 1
            
            ans[idx] = rank
            prev = val

        return ans


        """
        :type arr: List[int]
        :rtype: List[int]
        """
        