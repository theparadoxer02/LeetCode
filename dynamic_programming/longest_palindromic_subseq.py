def longestPalindromeSubseq(s: str) -> int:
    M = len(s)
    N = len(s)

    mem_matrix = [[-1] * (N + 1) for _ in range(M+1)]

    def get_longest_val(x, y, m, n):

        if mem_matrix[m][n] != -1:
            return mem_matrix[m][n] 

        if m == 0 or n == 0:
            mem_matrix[m][n] = 0
            return 0

        if x[m-1] == y[n-1]:
            mem_matrix[m][n] = 1 + get_longest_val(x, y, m-1, n-1)
        else:
            mem_matrix[m][n] = max(get_longest_val(x, y, m-1, n), get_longest_val(x, y, m, n-1))

        return mem_matrix[m][n]

    return get_longest_val(s, s[::-1], M, N)



def longestPalindromeSubseqTopDown(s: str) -> int:
    M = len(s)
    N = len(s)
    rev_s = s[::-1]

    mem_matrix = [[0] * (N + 1) for _ in range(M+1)]


    for i in range(1, M+1):
        for j in range(1, N+1):
            if s[i-1] == rev_s[j-1]:
                mem_matrix[i][j] = 1 + mem_matrix[i-1][j-1]
            else:
                mem_matrix[i][j] = max(mem_matrix[i-1][j], mem_matrix[i][j-1])
    
    return mem_matrix[i][j]


s = "leetcode"
result = longestPalindromeSubseqTopDown(s)


print(result)
