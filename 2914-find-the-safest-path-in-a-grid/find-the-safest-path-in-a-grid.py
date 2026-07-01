from collections import deque
import heapq


class Solution(object):

    def __init__(self):
        self.dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def maximumSafenessFactor(self, mat):

        n = len(mat)

        q = deque()

        # Copy matrix into grid
        grid = [[0] * n for _ in range(n)]

        # Collect all thief cells
        for i in range(n):
            for j in range(n):
                grid[i][j] = mat[i][j]

                if mat[i][j] == 1:
                    q.append((i, j))

        # ----------------------------
        # Multi-source BFS
        # ----------------------------
        while q:

            x, y = q.popleft()

            for dx, dy in self.dir:

                r = x + dx
                c = y + dy

                if (
                    r < 0 or r >= n or
                    c < 0 or c >= n or
                    grid[r][c] > 0
                ):
                    continue

                grid[r][c] = grid[x][y] + 1
                q.append((r, c))

        # ----------------------------
        # Dijkstra (Max Heap)
        # ----------------------------
        pq = []

        # Python heap is min heap,
        # use negative values for max heap
        heapq.heappush(
            pq,
            (-grid[0][0], 0, 0)
        )

        # Mark visited
        grid[0][0] = -1

        while pq:

            neg_sfac, x, y = heapq.heappop(pq)

            sfac = -neg_sfac

            # Reached destination
            if x == n - 1 and y == n - 1:
                return sfac - 1

            for dx, dy in self.dir:

                r = x + dx
                c = y + dy

                if (
                    r < 0 or r >= n or
                    c < 0 or c >= n or
                    grid[r][c] < 0
                ):
                    continue

                # Bottleneck value
                mn = min(sfac, grid[r][c])

                heapq.heappush(
                    pq,
                    (-mn, r, c)
                )

                # Mark visited
                grid[r][c] = -1

        return 0