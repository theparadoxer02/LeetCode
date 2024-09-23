def countSubstrings(s: str) -> int:
    M = len(s)
    mem_matrix = [[-1] * M for _ in range(M)]
    count = 0

    for i in range(M):
        mem_matrix[i][i] = 1
        count += 1

    for i in range(M - 1):
        if s[i] == s[i + 1]:
            mem_matrix[i][i + 1] = 1
            count += 1

    for i in range(M - 2, -1, -1):
        for j in range(i + 2, M): 
            if s[i] == s[j] and mem_matrix[i + 1][j - 1] == 1:
                mem_matrix[i][j] = 1
                count += 1

    return count


s = "babad"
result = countSubstrings(s=s)
print(result)
