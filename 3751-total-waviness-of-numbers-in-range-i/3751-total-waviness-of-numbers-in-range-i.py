class Solution(object):
    def totalWaviness(self, num1, num2):
        ans = 0

        for num in range(num1, num2+1):
            ans += self.getWaviness(num)
        return ans
    
    def getWaviness(self,num):
        count = 0
        s = str(num) # convert number to string
        for i in range(1,len(s)-1): # check the middle element
            if ((s[i] > s[i-1] and s[i] > s[i+1]) or 
            (s[i] < s[i-1] and s[i] < s[i+1])):
                count+=1
        return count        
        