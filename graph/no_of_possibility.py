
# def checkifvalid(char1, char2):
#     if char1 == "0":
#         return False
#     return "A" <= f"{char1}{char2}" <= "Z"


# def calc_possibility(input_str):
#     n = len(input_str)
#     counter = 1
#     for i in range(1, n):
#         if checkifvalid(input_str[i-1], input_str[i]):
#             counter += 1
#         else:
#             counter -= 1

#     return counter


# input_str = "11106"

# result = calc_possibility(input_str=input_str)
# print(result)



# 2. There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner. 
# Example 1:

# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


def no_of_ways(m, n):
    def solve(i, j):

        if i >= m or j >= n:
            return 0

        if i == m - 1 and j == n-1:
            return 1

        can_move_down = solve(i + 1, j)
        can_move_right = solve(i, j+1)

        return can_move_down + can_move_right

    return solve(0, 0)


result = no_of_ways(10, 1)
print(result)


