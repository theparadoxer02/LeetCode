from typing import List


def printLongestCommonSubSeq(nums1: List[int], nums2: List[int]) -> str:
    ''' Top down approach '''
    M = len(nums1)
    N = len(nums2)

    mem_matrix = [[0] * (N + 1) for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            if nums1[i-1] == nums2[j-1]:
                mem_matrix[i][j] = mem_matrix[i-1][j-1] + 1
            else:
                mem_matrix[i][j] = max(mem_matrix[i-1][j], mem_matrix[i][j-1])

    t = ""
    while i > 0 and j > 0:
        if nums1[i-1] == nums2[j-1]:
            t += nums1[i-1]
            i -= 1
            j -= 1
        else:
            if mem_matrix[i][j-1] > mem_matrix[i-1][j]:
                j -= 1
            else:
                i -= 1

    return t[::-1]


str1 = "ABCBDAB"
str2 = "BDCAB"


# output should be BCAB
result = printLongestCommonSubSeq(str1, str2)
print(result)
