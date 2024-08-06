def judgeSquareSum(c):

    def binary_search(low, high, c):
        if low > high:
            return False

        mid = (high + low) // 2
        
        result = (mid * mid)

        if result == c:
            return True

        if c > result:
            low = mid + 1
        else:
            high = mid - 1
        
        return binary_search(low, high, c)

    
    for a in range(0, c):
        b = c - a * a
        if binary_search(0, b, b):
            return True
        
    return False


output = judgeSquareSum(1)
print(output)


# Simply do two pointer where start is 0 and the end is sqrt of c(as we have to iterate till sqrt of c ).
# If sum (a^2+b^2) is equal to the sum then return true ;
# Else if sum is greater than c then decrease the end ;
# Else if sum is smaller than c then increase then start;
