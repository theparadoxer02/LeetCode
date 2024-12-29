from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        right = left + k
        window_set = set(nums[left:left+k])

        curr_sum = sum(window_set)
        max_sum = 0

        while right < N:
            if nums[right] in window_set:
                right += 1
                left += 1
                continue

            curr_sum = curr_sum - nums[left] + nums[right]
            max_sum = max(max_sum, curr_sum)
            window_set.add(nums[right])
            right += 1
            left += 1

        return max_sum


s = Solution()
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
result = s.maximumSubarraySum(nums=nums, k=k)
print(result)
