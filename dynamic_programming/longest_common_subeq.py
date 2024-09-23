def longestCommonSubsequence(text1: str, text2: str) -> int:

    M = len(text1)
    N = len(text2)

    mem_matrix = [[-1] * (N + 1) for _ in range(M+1)]

    def get_longest_val(x, y, m, n):

        if mem_matrix[m][n] != -1:
            print(x[m], y[n])
            return mem_matrix[m][n]

        if m == 0 or n == 0:
            mem_matrix[m][n] = 0
            return 0

        if x[m-1] == y[n-1]:
            return 1 + get_longest_val(x, y, m-1, n-1)
        else:
            mem_matrix[m][n] = max(get_longest_val(x, y, m-1, n), get_longest_val(x, y, m, n-1))

        return mem_matrix[m][n]

    return get_longest_val(text1, text2, M, N)


def longest_common_subsequence(x, y):
    m, n = len(x), len(y)
    # Create a 2D array with (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]



# Top Down approach
text1 = "abcde"
text2 = "ace"
result = longest_common_subsequence(x=text1, y=text2)
print(result)