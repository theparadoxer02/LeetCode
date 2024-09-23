from typing import List, Optional



class Solution:
    def __init__(self):
        pass

    def spiralMatrix(self, m: int, n: int, headd) -> List[List[int]]:

        matrix = [[-1] * n for _ in range(m)]

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                if not headd:
                    break
                matrix[top][i] = headd.val
                headd = headd.next

            top += 1

            for i in range(top, bottom + 1):
                if not headd:
                    break
                matrix[i][right] = headd.val
                headd = headd.next

            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if not headd:
                        break
                    matrix[bottom][i] = headd.val
                    headd = headd.next

                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if not headd:
                        break
                    matrix[i][left] = headd.val
                    headd = headd.next

                left += 1

        return matrix


t = Solution()
m = 3
n = 5
head = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
result = t.spiralMatrix(m=m, n=n, head=head)
print(result)
