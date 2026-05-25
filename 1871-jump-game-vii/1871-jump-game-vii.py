class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        if s[n - 1] == '1':
            return False
        arr = [0] * n
        count = 0

        for i in range(n):
            count+=arr[i]
            if i == 0 or (s[i] == '0' and count > 0):
                if i + minJump < n:
                    arr[i+minJump]+=1
                if i + maxJump +1 < n:
                    arr[i+maxJump+1] -= 1
        return count>0