from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        NO_STATE = 0
        BUY = 1
        SELL = 2
        HOLD = 3
        COOLDOWN = 4

        M = len(prices)

        dp = [[-1] * (M+1) for _ in range(5)]

        def backtrack(i, prev_state):
            if i == M:
                return 0

            if dp[prev_state][i] != -1:
                return dp[i][prev_state]

            if prev_state == BUY:
                max_profit = max(
                    backtrack(i+1, HOLD),
                    backtrack(i + 1, SELL) + prices[i]
                )

            elif prev_state == SELL:
                max_profit = backtrack(i+1, COOLDOWN)
                
            elif prev_state == HOLD:
                max_profit =  max(
                    backtrack(i+1, SELL) + prices[i],
                    backtrack(i+1, HOLD)
                )
            
            elif prev_state == COOLDOWN:
                max_profit =  max(
                    backtrack(i+1, BUY) - prices[i],
                    backtrack(i+1, COOLDOWN),
                )
            else:
                max_profit =  max(
                    backtrack(i+1, BUY) - prices[i],
                    backtrack(i+1, COOLDOWN),
                )
                
            dp[prev_state][i] = max_profit
            return dp[prev_state][i]
        
        return backtrack(0, COOLDOWN)

S = Solution()
prices = [1, 2, 3, 0, 2]
# prices = [1, 2]
result = S.maxProfit(prices=prices)
print(result)
