from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        N = len(nums)

        final_array = set()

        for i in range(0, N-2):
            left = i + 1
            right = N-1
            target = 0 - nums[i]

            # if nums[left] + nums[right] + nums[i] == 0:
            #     temp = (nums[i], nums[left], nums[right])
            #     final_array.add(temp)

            while left < right:
                if nums[left] + nums[right] == target:
                    temp = (nums[i], nums[left], nums[right])
                    final_array.add(temp)

                if nums[left] + nums[right] > target:
                    right -= 1
                
                else:
                    left += 1

        return list(dict.fromkeys(final_array))


s = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 0]
result = s.threeSum(nums=nums)
print(result)
