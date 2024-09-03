def chalkReplacer(chalk: list[int], k: int) -> int:
    rest = k % sum(chalk)

    target = rest
    i = 0
    for i, elem in enumerate(chalk):
        target -= elem
        if target < 0:
            return i

    return -1


chalk = [5, 1, 5]
k = 22

# chalk = [3,4,1,2]
# k = 25
result = chalkReplacer(chalk=chalk, k=k)
print(result)
