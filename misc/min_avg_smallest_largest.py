def minimumAverage(nums: list[int]) -> float:
    nums.sort()

    t = []

    N = len(nums)

    for i in range(N // 2):
        val = (nums[i] + nums[N-i-1])/2
        t.append(val)

    return min(t)


nums = [7, 8, 3, 4, 15, 13, 4, 1]
minimum = minimumAverage(nums=nums)
print(minimum)
