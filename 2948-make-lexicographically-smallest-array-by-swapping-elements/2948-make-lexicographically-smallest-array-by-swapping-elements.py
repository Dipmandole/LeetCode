class Solution(object):

    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # Store (value, original_index)
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        result = [0] * n

        i = 0

        while i < n:

            # Find one connected group
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Values in this group
            values = []

            # Original indices in this group
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # Smallest values should go to smallest indices
            indices.sort()

            for k in range(len(values)):
                result[indices[k]] = values[k]

            i = j + 1

        return result