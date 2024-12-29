from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        index = 0
        total_time = 0

        while index < N:
            curr_index = index
            max_val = neededTime[index]
            group_total_time = neededTime[index]
            
            while curr_index < N-1 and colors[curr_index] == colors[curr_index+1]:
                curr_index += 1
                max_val = max(max_val, neededTime[curr_index])
                group_total_time += neededTime[curr_index]
                
            if curr_index > index:
                total_time += group_total_time - max_val

            index = curr_index + 1
    
        return total_time



S = Solution()
colors = "aaabbbabbbb"
neededTime = [3,5,10,7,5,3,5,5,4,8,1]


result = S.minCost(colors=colors, neededTime=neededTime)
print(result)
