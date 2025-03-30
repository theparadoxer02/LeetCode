from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum_so_far = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # To handle the case where a subarray itself equals `k`
        
        for num in nums:
            sum_so_far += num
            if (sum_so_far - k) in prefix_sum_count:
                count += prefix_sum_count[sum_so_far - k]
            prefix_sum_count[sum_so_far] += 1
        
        return count
    

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    nums = [1, 2, 3]
    k = 3
    
    result = solution.subarraySum(nums, k)
    print(f"Input array: {nums}")
    print(f"Target sum k: {k}")
    print(f"Number of subarrays with sum {k}: {result}")
