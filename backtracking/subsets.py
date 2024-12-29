# def subsets(nums):
#     if not nums:
#         return
    
#     length = len(nums)
#     map = {}
#     ds = set()
    
#     def backtrack(ds, map):
#         if len(ds) == length:
#             return ds
#         for i in range(0, length):
#             if i not in map:
#                 ds.add(nums[i])
#                 map[i] = 1
#                 backtrack(ds, map)

#     backtrack(ds=ds, map=map)


def subsets(nums):
    if not nums:
        return [[]]

    n = len(nums)

    first = nums[0]
    rest = nums[1:]

    rest_subsets = subsets(rest)
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append([first] + subset)

    return rest_subsets + new_subsets



def bitwise_subsets(nums):
    n = len(nums)
    result = []
    # Generate all possible subsets (2^n subsets)
    for i in range(2**n):  # Loop over 0 to 2^n - 1
        subset = []
        for j in range(n):  # Check each bit
            if (i >> j) & 1:  # If the j-th bit is set in i
                subset.append(nums[j])
        result.append(subset)
    return result


# Example usage
nums = [1, 2, 3]
print(subsets(nums))

nums = [2,5,6]
result = bitwise_subsets(nums=nums)
print(result)