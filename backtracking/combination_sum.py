# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

def combinationSum(candidates, target):

    def get_subsets(nums):
        if not nums:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        rest_subsets = get_subsets(rest)

        # if sum(rest_subsets) == target:
        #     ans.append(rest_subsets)

        new_subsets = []
        for subset in rest_subsets:
            value = [first] + subset
            new_subsets.append(value)

        return rest_subsets + new_subsets


    result = get_subsets(candidates)
    ans = []
    for elem in result:
        if sum(elem) == target:
            ans.append(elem) 
    return result



target = 7
candidates = [2,3,6,7]

result = combinationSum(candidates=candidates, target=target)
print(result)