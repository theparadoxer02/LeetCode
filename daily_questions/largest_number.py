from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_chars = 0
        for num in nums:
            max_chars = max(max_chars, len(str(num)))

        temp_array = []
        for index, num in enumerate(nums):
            str_num = str(num)
            str_num = str_num * (1 + max_chars - len(str_num))
            temp_array.append((index, str_num))

        sorted_array = sorted(temp_array, key=lambda x: x[1], reverse=True)

        final_str = ""
        for elem in sorted_array:
            final_str += str(nums[elem[0]])

        return final_str
        

s = Solution()
nums = [3, 30, 34, 5, 9]
result = s.largestNumber(nums=nums)

print(result)
