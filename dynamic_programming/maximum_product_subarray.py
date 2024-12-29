
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = float('-inf')
        minimum = float('inf')
        temp_min = 1
        temp_max = 1

        for num in nums:
            maximum = max(maximum, num * temp_max)
            minimum = min(minimum, num * temp_min)

            temp_max = num * temp_max
            temp_min = num * temp_min

            if maximum < 0:
                maximum = float('-inf')

        return max(maximum, minimum)

