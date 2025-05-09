import random


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        count = 0
        idx = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == 1:
                    idx = i
        return idx


s = Solution([1, 2, 3, 5, 3, 3])
result = s.pick(3)
s.pick(3)
s.pick(3)
print(result)
