from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        N = len(stones)
        stones = [0] + stones + [0]
        dp = [[-1] * N for _ in range(N)]

        if (N - 1) % (k - 1) != 0:
            return -1

        def solve(i, j):
            if i >= N or j >= N:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if i + 1 >= j:
                return 0

            min_stones = float('inf')
            for pt in range(i+1, j):
                temp_piles_sum = solve(i, pt) + sum(stones[i:j]) + solve(pt, j)
                min_stones = min(min_stones, temp_piles_sum)
            dp[i][j] = min_stones

            return dp[i][j]
        
        return solve(0, N-1)


s = Solution()
stones = [3, 2, 4, 1]
k = 2

result = s.mergeStones(stones=stones, k=k)
print(result)
