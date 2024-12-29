import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_weight = 0

        inMST = [False] * n
        heap = [(0, 0)]

        found_edge = 0

        while found_edge < n:
            weight, curr_node = heapq.heappop(heap)

            if inMST[curr_node]:
                continue

            found_edge += 1
            min_weight += weight
            inMST[curr_node] = True

            for next_node in range(n):
                if inMST[next_node]:
                    continue

                weight = abs(points[next_node][0] - points[curr_node][0]) + \
                    abs(points[next_node][1] - points[curr_node][1])

                heapq.heappush(heap, (weight, next_node))

        return min_weight
