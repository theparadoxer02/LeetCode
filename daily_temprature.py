from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        next_greater = []
        for index in range(N - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()

            if stack:
                next_greater.append(stack[-1] - index)
            else:
                next_greater.append(0)

            stack.append(index)

        next_greater.reverse()
        return next_greater


s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
result = s.dailyTemperatures(temperatures=temperatures)
print(result)
