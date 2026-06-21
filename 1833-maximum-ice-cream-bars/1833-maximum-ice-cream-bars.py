class Solution(object):
    def maxIceCream(self, costs, coins):

        # Frequency array
        count = [0] * 100001

        # Count occurrences of each cost
        for cost in costs:
            count[cost] += 1

        ans = 0

        # Buy ice creams starting from cheapest
        for i in range(1, len(count)):

            # No point continuing if we can't afford cost i
            if coins < i:
                break

            while count[i] > 0 and coins >= i:
                ans += 1
                count[i] -= 1
                coins -= i

        return ans
        