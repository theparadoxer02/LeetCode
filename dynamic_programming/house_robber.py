def rob(nums: list[int]) -> int:

    N = len(nums)
    W = sum(nums)

    mem_matrix = [[-1] * (W+1) for _ in range(N+1)]

    def knapsack(curr_index, curr_sum):
        if curr_index >= N:
            return curr_sum

        if mem_matrix[curr_index][curr_sum] != -1:
            return mem_matrix[curr_index][curr_sum]

        include_sum = knapsack(curr_index+2, curr_sum + nums[curr_index])
        exclude_sum = knapsack(curr_index+1, curr_sum)

        mem_matrix[curr_index][curr_sum] = max(include_sum, exclude_sum)
        return mem_matrix[curr_index][curr_sum]

    return knapsack(0, 0)


def robusingSingleDimension(nums: list[int]) -> int:
    N = len(nums)
    mem_matrix = [-1] * N

    def knapsack(curr_index):
        if curr_index >= N:
            return 0

        if mem_matrix[curr_index] != -1:
            return mem_matrix[curr_index]

        include_sum = knapsack(curr_index+2) + nums[curr_index]
        exclude_sum = knapsack(curr_index+1)

        mem_matrix[curr_index] = max(include_sum, exclude_sum)
        return mem_matrix[curr_index]

    return knapsack(0)


def rob(self, nums: list[int]) -> int:
    N = len(nums)
    if N == 0:
        return 0
    if N == 1:
        return nums[0]
    mem_matrix = [0] * N
    mem_matrix[0] = nums[0]
    mem_matrix[1] = max(nums[0], nums[1])

    def robusingTabular():
        for i in range(2, N):
            include_sum = mem_matrix[i-2] + nums[i]
            exclude_sum = mem_matrix[i-1]
            mem_matrix[i] = max(include_sum, exclude_sum)

        return mem_matrix[-1]

    return robusingTabular()


nums = [1, 2, 3, 1]
result = rob(nums=nums)
print(result)
