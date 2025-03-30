from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length

        # left iteration
        left[0] = 1
        mult = 1
        for index in range(length)[1:]:
            mult = nums[index-1] * mult
            left[index] = mult
    
        right[length-1] = 1
        mult_right = 1
        for index in range(length-1)[::-1]:
            mult_right = nums[index+1] * mult_right
            right[index] = mult_right

        final = []
        for i in range(length):
            print(left[i], right[i])
            final.append(left[i] * right[i])

        return final


s = Solution()
nums = [1, 2, 3, 4]

result = s.productExceptSelf(nums=nums)
print(result)
