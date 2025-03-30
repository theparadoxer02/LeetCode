from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxi_window = deque()

        for index in range(len(nums)):
            if maxi_window and maxi_window[0] < index - k + 1:
                maxi_window.popleft()

            while maxi_window and nums[index] > nums[maxi_window[-1]]:
                maxi_window.pop()

            maxi_window.append(index)

            if index >= k - 1:
                result.append(nums[maxi_window[0]])

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
result = s.maxSlidingWindow(nums=nums, k=k)
print(result)
