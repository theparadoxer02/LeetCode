class Solution:
    def jump(self, nums):
        N = len(nums)
        if N <= 1:
            return 0

        l, r = 0, nums[0]
        times = 1

        while r < N - 1:
            times += 1
            tt = []
            for i in range(l, r + 1):
                tt.append(i + nums[i])

            nxt = max(tt)
            l, r = r, nxt
        return times


input_nums = [2, 3, 1, 1, 4]
s = Solution()
result = s.jump(nums=input_nums)
print(result)
