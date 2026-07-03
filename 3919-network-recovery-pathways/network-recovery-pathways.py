import heapq
from collections import defaultdict


class Solution(object):

    def findMaxPathScore(self, edges, online, k):

        self.hmap = defaultdict(list)
        n = len(online)

        max_edge = 0

        # Build graph using only online nodes
        for src, dest, cost in edges:

            if not online[src] or not online[dest]:
                continue

            self.hmap[src].append((dest, cost))
            max_edge = max(max_edge, cost)

        # Binary Search on answer
        left = 0
        right = max_edge
        ans = -1

        while left <= right:

            mid = left + (right - left) // 2

            if self.dijkstra(mid, k, n):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def dijkstra(self, min_edge, k, n):

        dist = [float('inf')] * n
        dist[0] = 0

        # (cost_so_far, node)
        pq = [(0, 0)]

        while pq:

            cost_so_far, node = heapq.heappop(pq)

            # Skip stale entries
            if cost_so_far > dist[node]:
                continue

            # Reached destination
            if node == n - 1:
                return cost_so_far <= k

            if node not in self.hmap:
                continue

            for nxt, edge_cost in self.hmap[node]:

                # Ignore edges below threshold
                if edge_cost < min_edge:
                    continue

                next_cost = cost_so_far + edge_cost

                # Budget pruning
                if next_cost > k:
                    continue

                if next_cost < dist[nxt]:
                    dist[nxt] = next_cost
                    heapq.heappush(
                        pq,
                        (next_cost, nxt)
                    )

        return False