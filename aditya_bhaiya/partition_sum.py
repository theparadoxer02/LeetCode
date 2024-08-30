def canPartition(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0:
        return False

    n = len(nums)
    target_sum = sum(nums) // 2
    memmatrix = [[-1] * (target_sum + 1) for _ in range(n + 1)]

    def knapsack(currIndex, curr_sum):

        if curr_sum == target_sum:
            return True

        if not 0 <= currIndex < n:
            return False
        
        if curr_sum > target_sum or curr_sum < 0:
            return False

        if memmatrix[currIndex][curr_sum] != -1:
            return memmatrix[currIndex][curr_sum]

        if knapsack(currIndex+1, curr_sum + nums[currIndex]):
            memmatrix[currIndex][curr_sum] = True
            return True

        if knapsack(currIndex+1, curr_sum):
            memmatrix[currIndex][curr_sum] = True
            return True

        memmatrix[currIndex][curr_sum] = False
        return False

    return knapsack(0, curr_sum=0)