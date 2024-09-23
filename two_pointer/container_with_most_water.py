from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left = 0
        # right = N-1
        max_area = 0

        for
        # while left <= right and left <= 0 and right < N:
        while left > 0 and height[left - 1] < height[i]:
            left -= 1
        
        while right < N-1 and height[right + 1] < height[i]:
            right += 1
        
        area = (right +1 - left) * height[i]
        if i == 4:
            3
        print(area)


s = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = s.maxArea(height=height)
print(result)


