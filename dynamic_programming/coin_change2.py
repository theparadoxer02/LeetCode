def coinChange(coins: list[int], amount: int) -> int:

    N = len(coins)

    mem_matrix = [[-1] * amount for _ in range(N + 1)]

    def knapsack(curr_index, curr_sum):
        if curr_sum == amount:
            return 1

        if curr_index == N:
            return 0

        if curr_sum > amount:
            return 0

        if mem_matrix[curr_index][curr_sum] != -1:
            return mem_matrix[curr_index][curr_sum]

        include_count = knapsack(curr_index, curr_sum + coins[curr_index])
        exclude_count = knapsack(curr_index + 1, curr_sum)

        mem_matrix[curr_index][curr_sum] = include_count + exclude_count

        return mem_matrix[curr_index][curr_sum]

    return knapsack(0, curr_sum=0)


coins = [1, 2, 5]
amount = 5
result = coinChange(coins=coins, amount=amount)
print(result)
