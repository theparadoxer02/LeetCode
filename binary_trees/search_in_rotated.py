from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def get_pivot_value(left, right):
            while left < right:
                middle = (left + right) // 2

                if nums[middle] > nums[right]:
                    left = middle + 1
                else:
                    right = middle

            return left

        pivot_index = get_pivot_value(0, len(nums)-1)
        return pivot_index




s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = s.search(nums=nums, target=target)
print(result)

