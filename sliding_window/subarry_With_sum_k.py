from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        curr_sum = 0
        k_sum_count = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            if curr_sum == k:
                k_sum_count += 1

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == k:
                k_sum_count += 1

        return k_sum_count


s = Solution()
nums = [1]
k = 0
result = s.subarraySum(nums=nums, k=k)
print(result)
