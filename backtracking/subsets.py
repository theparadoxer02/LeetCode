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

nums = [1,2,3]
result = subsets(nums=nums)
print(result)