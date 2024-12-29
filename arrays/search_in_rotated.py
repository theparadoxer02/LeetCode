def findMin(nums) -> int:
    def binary_search(nums, l, r, minimum):
        if l > r:
            return minimum

        mid = (l + r) // 2

        if minimum > nums[mid]:
            minimum = nums[mid]

        print(f"l {l}, r: {r}, minimum: {minimum}")
        if nums[l] <= nums[mid]:
            minimum = min(minimum, nums[l])
            return binary_search(nums, mid + 1, r, minimum)
        else:
            minimum = min(minimum, nums[mid])
            return binary_search(nums, l, mid - 1, minimum)

    if not nums:
        return -1  # Handle the case where nums is an empty list.

    l, r = 0, len(nums) - 1
    minimum = nums[0]

    return binary_search(nums, l, r, minimum)

nums = [3,4,5,1,2]


result = findMin(nums)
print(result)

    

    l, r = 0, len(nums) - 1    

    return binary_search(nums, l , r)



nums = [1,3]
target = 3


search_result = search(nums, target)
print(search_result)