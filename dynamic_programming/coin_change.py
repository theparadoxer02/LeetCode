def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    if not coins:
        return 0

    N = len(coins)
    mem_matrix = [[-1] * (amount + 1) for _ in range(N + 1)]

    def knapsack(curr_index, curr_sum):
        if curr_sum == amount:
            return 0

        if curr_index == N:
            return float('inf')

        if curr_sum > amount:
            return float('inf')

        if mem_matrix[curr_index][curr_sum] != -1:
            return mem_matrix[curr_index][curr_sum]

        include_count = 1 + knapsack(curr_index, curr_sum + coins[curr_index])
        exclude_count = knapsack(curr_index + 1, curr_sum)

        mem_matrix[curr_index][curr_sum] = min(include_count, exclude_count)

        return mem_matrix[curr_index][curr_sum]

    return knapsack(0, curr_sum=0)


coins = [1, 2, 5]
amount = 11

# coins = [2]
# amount = 3

coins = [1]
amount = 0
result = coinChange(coins=coins, amount=amount)
print(result)
