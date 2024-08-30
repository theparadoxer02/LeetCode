def findTargetSumWays(nums: list[int], target: int) -> int:
    if not nums:
        return 0

    N = len(nums)

    mem_matrix = [[-1] * target for _ in range(N + 1)]

    def knapsack(curr_index, curr_sum):
        if curr_sum == target:
            return 1

        if curr_index == N:
            return 0

        if curr_sum > target:
            return 0

        if mem_matrix[curr_index][curr_sum] != -1:
            return mem_matrix[curr_index][curr_sum]

        include_count = knapsack(curr_index + 1, curr_sum + nums[curr_index])
        exclude_count = knapsack(curr_index + 1, curr_sum)

        mem_matrix[curr_index][curr_sum] = min(include_count, exclude_count)

        return mem_matrix[curr_index][curr_sum]

    return knapsack(0, curr_sum=0)


nums = [1, 2, 1]
target = 0
result = findTargetSumWays(nums=nums, target=target)
print(result)
