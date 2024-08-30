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



# Top Down approach
text1 = "abcde"
text2 = "ace" 
result = longestCommonSubsequence(text1=text1, text2=text2)
print(result)