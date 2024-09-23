from typing import List


class Solution:
    def __init__(self):
        pass

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])

        top = 0
        bottom = M - 1
        left = 0
        right = N - 1

        sprial_array = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                sprial_array.append(matrix[top][i])

            top += 1

            for i in range(top, bottom+1):
                sprial_array.append(matrix[i][right])

            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    sprial_array.append(matrix[bottom][i])

                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    sprial_array.append(matrix[i][left])

                left += 1

        return sprial_array

t = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = t.spiralOrder(matrix=matrix)
print(result)
