def getLucky(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    letter_to_number = {chr(i): i - 96 for i in range(97, 123)}

    def iter_vals(s):
        final = ""
        for char in s:
            final += str(letter_to_number.get(char))
        
        final_int = sum(int(i) for i in final)

        return str(final_int)

    sum_val = iter_vals(s)
    for _ in range(k-1):
        t = 0
        for char in sum_val:
            t += int(char)
        
        sum_val = str(t)
    return int(sum_val)
    print(s)


s = "zbax"
k = 2
result = getLucky(s, k)
print(result)