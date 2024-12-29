from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        right = 0
        curr_sum = 0
        max_sum = 0

        window_dict = {}
        ignored = set()

        while right < N:
            window_dict[right] += 1

            while left in ignored:
                left += 1

            curr_sum = curr_sum - nums[left] + nums[right]
            max_sum = max(max_sum, curr_sum)
            right += 1

        return max_sum


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
S = Solution()
result = S.maximumSubarraySum(nums=nums, k=k)
print(result)
