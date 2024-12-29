class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        dp = [[-1] * (N + 1) for _ in range(M + 1)]

        def backtracking(i, j, word1, word2, m, n, dp):
            if i == m and j == n:
                return 0

            if i == m:
                return n - j
            if j == n:
                return m - i

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = backtracking(i+1, j+1, word1, word2, m, n, dp)
            else:
                insert_count = 1 + backtracking(i, j + 1, word1, word2, m, n, dp)
                delete_count = 1 + backtracking(i + 1, j, word1, word2, m, n, dp)
                replace_count = 1 + backtracking(i + 1, j + 1, word1, word2, m, n, dp)

                dp[i][j] = min(insert_count, delete_count, replace_count)
            return dp[i][j]

        return backtracking(0, 0, word1, word2, M, N, dp)


S = Solution()
word1 = "intention"
word2 = "execution"

result = S.minDistance(word1, word2)
print(result)
