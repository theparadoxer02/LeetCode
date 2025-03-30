from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left = right = 0
        curr_sum = 1
        final_count = 0

        for right in range(len(nums)):
            curr_sum *= nums[right]

            while curr_sum >= k:
                curr_sum //= nums[left]
                left += 1
                
            final_count += (right - left + 1)

        return final_count


s = Solution()
nums = [10, 5, 2, 6]
k = 100

# nums = [1,2,3]
# k = 0
result = s.numSubarrayProductLessThanK(nums=nums, k=k)
print(result)

