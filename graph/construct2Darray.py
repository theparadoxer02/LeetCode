def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    N = len(original)
    if m * n != len(original):
        return []
    
    final = []
    break_point = 0
    for i in range(1, n+1):
        if i % n == 0:
            final.append(original[break_point:i])
            break_point = i
    print(final)
    return final
    

result = construct2DArray([1,2,3,4], 2, 2)
print(result)