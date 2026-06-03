class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        bestLandFinsh = float('inf')
        bestWaterFinsh = float('inf')
        ans = float('inf')

        for i in range(len(landStartTime)):
            bestLandFinsh = min(bestLandFinsh, landStartTime[i] + landDuration[i])
        
        for i in range(len(waterStartTime)):
            finishTime = max(bestLandFinsh, waterStartTime[i]) + waterDuration[i]
            ans = min(ans, finishTime)
        

        for i in range(len(waterStartTime)):
            bestWaterFinsh = min(bestWaterFinsh, waterStartTime[i] + waterDuration[i])
        
        for i in range(len(landStartTime)):
            finishTime = max(bestWaterFinsh, landStartTime[i]) + landDuration[i]
            ans = min(ans, finishTime)
        return ans