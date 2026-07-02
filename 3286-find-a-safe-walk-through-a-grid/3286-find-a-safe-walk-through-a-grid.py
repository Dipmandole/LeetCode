import heapq


class Solution(object):
    def findSafeWalk(self, arr, health):

        m = len(arr)
        n = len(arr[0])

        # Make a copy because we'll mark cells as visited
        grid = [row[:] for row in arr]

        # Min Heap: [cost_so_far, row, col]
        pq = []

        heapq.heappush(pq, (grid[0][0], 0, 0))

        # Mark start as visited
        grid[0][0] = float('inf')

        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]

        while pq:

            cost, x, y = heapq.heappop(pq)

            # Reached destination
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions:

                r = x + dx
                c = y + dy

                # Out of bounds
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue

                # Already visited
                if grid[r][c] == float('inf'):
                    continue

                # Not enough health to enter this cell
                if health - grid[r][c] <= 0:
                    continue

                next_cost = cost + grid[r][c]

                if next_cost < health:
                    heapq.heappush(
                        pq,
                        (next_cost, r, c)
                    )

                # Mark visited
                grid[r][c] = float('inf')

        return False