def maximumSubarraySum(nums, k):
    def subsets(nums):
        if not nums:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        rest_subsets = subsets(rest)
        new_subsets = []
        for subset in rest_subsets:
            new_subsets.append([first] + subset)

        return rest_subsets + new_subsets

    max_subset_sum = 0
    total_subsets = subsets(nums=nums)
    for subset in total_subsets:
        if subset and abs(subset[0] - subset[-1]) == k:
            max_subset_sum = max(max_subset_sum, sum(subset))

    return max_subset_sum


nums = [1, 2, 3, 4, 5, 6]
result = maximumSubarraySum(nums=nums, k=1)
print(result)
