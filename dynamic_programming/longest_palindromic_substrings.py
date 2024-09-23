from typing import List


def longestPalindromicSubStringTopDown(s: str) -> str:
    M = len(s)
    mem_matrix = [[-1] * M for _ in range(M)]
    longest_substring = ""

    for i in range(M):
        mem_matrix[i][i] = 1

    for i in range(M - 1):
        if s[i] == s[i + 1]:
            mem_matrix[i][i + 1] = 1
            longest_substring = s[i:i+2]

    for i in range(M - 2, -1, -1):
        for j in range(i + 2, M):
            if s[i] == s[j] and mem_matrix[i + 1][j - 1] == 1:
                mem_matrix[i][j] = 1

                if len(s[i:j+1]) > len(longest_substring):
                    longest_substring = s[i:j+1]
    return longest_substring








def longestPalindrome(ses: str) -> str:
    M = len(s)
    mem_matrix = [[False] * M for _ in range(M)]
    ans = [0, 0]

    for i in range(M):
        mem_matrix[i][i] = True


    for i in range(M - 1):
        if s[i] == s[i + 1]:
            mem_matrix[i][i + 1] = True
            ans = [i, i + 2]

    for i in range(M - 2, -1, -1):
        for j in range(i + 2, M):
            if s[i] == s[j] and mem_matrix[i + 1][j - 1] == 1:
                mem_matrix[i][j] = True
                ans = [i, j]
    i, j = ans
    return s[i : j + 1]




str1 = "cbbd"
result = longestPalindrome(str1)
print(result)


