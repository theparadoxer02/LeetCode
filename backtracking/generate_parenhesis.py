from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        def inner(string, start, close):
            if not close:
                stack.append(string)
                return

            if start:
                inner(string + '(', start - 1, close)

            if close > start:
                inner(string + ')', start, close - 1)

        inner('(', n, n-1)
        return stack


S = Solution()
n = 3
result = S.generateParenthesis(3)
print(result)