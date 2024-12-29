def minEatingSpeed(piles, hours):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    

    def binary_search(start, end):
        if start >= end:
            return start

        mid = (start + end) // 2

        finished = can_finish_piles(mid, piles)
        if finished:
            end = mid
        else:
            start = mid + 1  
        return binary_search(start, end)


    def can_finish_piles(banana_per_hour, piles, hours):
        total_hours = 0

        for pile in piles:
            total_hours += (pile + banana_per_hour - 1) // banana_per_hour

        # if the piles is finished early
        return total_hours <= hours
 
        
    start = 1
    end = max(piles)
    binary_search(start, end)


piles = [3,6,7,11]
h = 8
result = minEatingSpeed(piles, h)
print(result)