def climbStairs(n: int) -> int:

    mem_z = [-1] * (n + 1)
    mem_z[0], mem_z[1], mem_z[2] = 0, 1, 2

    def climb(target):
        if mem_z[target] != -1:
            return mem_z[target]

        one_step_count = climb(target-1)
        two_step_count = climb(target-2)

        mem_z[target] = one_step_count + two_step_count
        return mem_z[target]

    return climb(n)


result = climbStairs(4)
print(result)