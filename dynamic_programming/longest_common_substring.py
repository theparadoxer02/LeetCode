from typing import List


def longestCommonSubStringTopDown(self, nums1: List[int], nums2: List[int]) -> int:
    ''' Top down approach '''
    M = len(nums1)
    N = len(nums2)

    mem_matrix = [[0] * (N + 1) for _ in range(M+1)]
    max_val = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if nums1[i-1] == nums2[j-1]:
                mem_matrix[i][j] = mem_matrix[i-1][j-1] + 1
                max_val = max(max_val, mem_matrix[i][j])

    return max_val


def longestCommonSubString(text1: str, text2: str) -> int:
    M = len(text1)
    N = len(text2)

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
            mem_matrix[m][n] = 0

        return mem_matrix[m][n]

    max_length = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if text1[i-1] == text2[j-1]:
                if mem_matrix[i][j] == -1:
                    get_longest_val(text1, text2, i, j)
                max_length = max(max_length, mem_matrix[i][j])

    return max_length


nums1 = "12321"
nums2 = "32147"


# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4]
result = longestCommonSubString(text1=nums1, text2=nums2)
print(result)



# "eleetminicoworoep"


# "leetminicowor"