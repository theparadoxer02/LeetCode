# JobTwine Interviewer
# Input: N = “218765”
# Output: “251678”
# Explanation: The next number greater than 218765 with same set of digits is 251678.


# Input: n = “1234”
# Output: “1243”
# Explanation: The next number greater than 1234 with same set of digits is 1243.


# Input: n = “4321”
# not possible


# input n = "2398761"
"2613789"


# n = "2487631"


# 2487631
"2613478"

# 3 248761
"3124678"


def sovle(s):
    left = 0
    right = len(s) - 1

    while right > 0 and s[right-1] >= s[right]:
        right -= 1

    left = right

    # keep moving left till you hit the first hight value than itsenf
    swap_index = right - 1
    swap_val = s[right]
    min_val = float("-inf")
    # swap_index = right
    while left < len(s):
        if s[left] > swap_val:
            min_val = min(min_val, s[left])
        left += 1

    s[swap_index], s[left] = s[left], s[swap_index]

    rest_val = s[swap_index+1:].sort()
    final_string = s[:swap_index+1].extend(rest_val)

    return final_string
