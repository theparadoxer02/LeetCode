def minCostClimbingStairs(cost: list[int]) -> int:
    N = len(cost)

    mem_z = [-1] * N

    def climbStairs(curr_ind):

        if curr_ind >= N:
            return 0

        if mem_z[curr_ind] != -1:
            return mem_z[curr_ind]
        
        one_jump = cost[curr_ind] + climbStairs(curr_ind + 1)
        two_jump = cost[curr_ind] + climbStairs(curr_ind + 2)

        mem_z[curr_ind] = min(one_jump, two_jump)

        return mem_z[curr_ind]

    abc = climbStairs(curr_ind=0)
    xyz = climbStairs(curr_ind=1)
    
    return min(abc, xyz)


cost = [10, 15, 20]

result = minCostClimbingStairs(cost=cost)
print(result)
