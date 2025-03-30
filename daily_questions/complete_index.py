from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        filled_row = [0] * m
        filled_cols = [0] * n

        find_index = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == arr[find_index]:
                    find_index += 1
                    filled_row[i] += 1
                    filled_cols[j] += 1
                    print(find_index, filled_row, filled_cols)

                    if filled_row[i] == m or filled_cols[j] == n:
                        return find_index
        return -1


arr = [1, 3, 4, 2]
mat = [[1, 4], [2, 3]]
s = Solution()

result = s.firstCompleteIndex(arr=arr, mat=mat)
print(result)
