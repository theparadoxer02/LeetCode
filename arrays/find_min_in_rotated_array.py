def findMin(nums) -> int:


    
    def binary_search(nums, l , r, minimum):
        if l > r:
            return minimum
        
        mid = (l + r) // 2

        if minimum > nums[mid]:
            minimum = nums[mid]
        
    
        if nums[l] <= nums[mid]:
            minimum = min(minimum, nums[l])
            l = mid + 1

        else:
            minimum = min(minimum, nums[mid])
            r = mid - 1

        return binary_search(nums, l , r, minimum)

    l, r = 0, len(nums) - 1   

    minimum = nums[0]

    return binary_search(nums, l , r, minimum)
    
nums = [4,5,6,7,0,1,2]





print(findMin(nums=nums))