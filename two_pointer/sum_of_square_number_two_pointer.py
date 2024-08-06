def judgeSquareSum(c):

    def binary_search(low, high, c):
        if low > high:
            return high

        mid = (high + low) // 2
        
        result = (mid * mid)

        if result == c:
            return mid

        if c > result:
            low = mid + 1
        else:
            high = mid - 1
        
        return binary_search(low, high, c)

    closed_sql_root_value = binary_search(0, c, c)
    

    left = 0
    right = closed_sql_root_value
    while left <= right:
        temp_sum = left * left + right * right
        if temp_sum == c:
            return True

        if temp_sum > c:
            right -= 1
        
        elif temp_sum < c:
            left += 1

    return False



output = judgeSquareSum(1)
print(output)


# Simply do two pointer where start is 0 and the end is sqrt of c(as we have to iterate till sqrt of c ).
# If sum (a^2+b^2) is equal to the sum then return true ;
# Else if sum is greater than c then decrease the end ;
# Else if sum is smaller than c then increase then start;
