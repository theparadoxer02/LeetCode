def uniquePaths(m: int, n: int) -> int:

    mem_matrix = [[-1] * (n+1) for _ in range(m+1)]

    def knapsac(curr_i, curr_j):

        if mem_matrix[curr_i][curr_j] != -1:
            return mem_matrix[curr_i][curr_j]

        if curr_i >= m or curr_j >= n:
            return 1

        right_step = 1 + knapsac(curr_i + 1, curr_j)
        down_step = 1 + knapsac(curr_i, curr_j + 1)

        mem_matrix[curr_i][curr_j] = right_step + down_step

        return mem_matrix[curr_i][curr_j]

    return knapsac(0, 0)


m = 3
n = 7
result = uniquePaths(m, n)
print(result)
