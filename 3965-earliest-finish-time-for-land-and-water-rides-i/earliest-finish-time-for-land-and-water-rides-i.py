class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)
        mini = float("inf")

        for i in range(n):
            for j in range(m):
                land_cost = landStartTime[i] + landDuration[i]
                water_cost = waterStartTime[j] + waterDuration[j]
                case1 = land_cost + max(0, waterStartTime[j] - land_cost) + waterDuration[j]
                case2 = water_cost + max(0, landStartTime[i] - water_cost) + landDuration[i]
                mini = min(mini,case1,case2)
        return mini