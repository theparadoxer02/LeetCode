from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]

            if numbers[left] + numbers[right] > target:
                right -= 1
            
            if numbers[left] + numbers[right] < target:
                left += 1

        return False

s = Solution()
numbers = [2,7,11,15]
target = 9
result = s.twoSum(numbers=numbers, target=target)
print(result)
