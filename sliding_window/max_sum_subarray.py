from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return

        N = len(nums)

        if N == 2:
            if nums[0] > 0 and nums[1] > 0:
                return sum(nums)
            else:
                return max(nums)

        curr_sum = nums[0]
        max_sum = 0
        left = 0
        right = 1

        while right < N:
            val = curr_sum - nums[left] + nums[right]
            if val > max_sum:
                max_sum = val
                left = right
            right += 1
        
        return max_sum


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = s.maxSubArray(nums=nums)
print(result)
