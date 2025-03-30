# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         N = len(nums)
#         if not nums:
#             return [-1, -1]
        
#         def binary_search(nums, left, right, target):
#             if left > right:
#                 return -1

#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid
            
#             if nums[mid] < target:
#                 left = mid + 1
            
#             if nums[mid] > target:
#                 right = mid - 1
            
#             return binary_search(nums, left, right, target)

#         mid_point = len(nums) // 2
#         leftmost = binary_search(nums, 0, N-1, target)
#         rightmost = binary_search(nums[::-1], 0, N-1, target)
        
#         if leftmost == -1 or rightmost == -1:
#             val = max(leftmost, rightmost)
#             return [val, val]

#         return [leftmost, N - rightmost]

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def right_most_binary_search(nums):
            N = len(nums)
            left = 0
            right = N - 1

            right_most = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    right_most = mid
                    left = mid + 1
            
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right_most

        def left_most_binary_search(nums):
            N = len(nums)
            left = 0
            right = N - 1

            left_most_index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    left_most_index = mid
                    right = mid - 1
            
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left_most_index

        right_most_index = right_most_binary_search(nums=nums)
        if right_most_index == -1:
            return [-1, -1]
        left_most_index = left_most_binary_search(nums=nums)
        return [left_most_index, right_most_index]


s = Solution()

nums = [5, 7, 7, 8, 8, 8, 8, 8, 8, 10]
target = 8

print(s.searchRange(nums, target))
