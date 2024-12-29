from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        stack = []
        next_small = []
        for elem in prices[::-1]:
            while stack and stack[-1] > elem:
                stack.pop()
            
            if stack:
                next_small.append(stack[-1])
            else:
                next_small.append(0)
            
            stack.append(elem)
        
        next_small.reverse()

        discounted = []
        for index in range(N):
            discounted.append(prices[index] - next_small[index])
        
        return discounted

s = Solution()
prices = [8, 4, 6, 2, 3]
result = s.finalPrices(prices=prices)
print(result)
