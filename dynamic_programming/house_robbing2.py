def rob(nums: list[int]) -> int:

    def robusingTabular(nums):
        N = len(nums)
        mem_matrix = [0] * N
        mem_matrix[0] = nums[0]
        mem_matrix[1] = max(nums[0], nums[1])

        for i in range(2, N):
            include_sum = mem_matrix[i-2] + nums[i]
            exclude_sum = mem_matrix[i-1]
            mem_matrix[i] = max(include_sum, exclude_sum)

        return mem_matrix[-1]

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)
    
    first_res = robusingTabular(nums=nums[0:-1])
    seond_res = robusingTabular(nums=nums[1:])
    return max(first_res, seond_res)


nums = [0,0]
result = rob(nums=nums)
print(result)