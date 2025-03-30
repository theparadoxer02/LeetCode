from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysToShip(capacity):
            days_to_port = 1
            weight_taken = 0

            for weight in weights:
                if weight_taken + weight > capacity:
                    days_to_port += 1
                    weight_taken = 0
                    
                weight_taken += weight

            return days_to_port

        cap_low = 1
        cap_high = sum(weights)
        lowest_cap = -1

        while cap_low <= cap_high:
            mid_cap = (cap_low + cap_high) // 2

            days_to_ship = daysToShip(mid_cap)

            print(days_to_ship, mid_cap)

            if days_to_ship == days:
                return mid_cap

            if days_to_ship > days:
                cap_low = mid_cap + 1

            if days_to_ship < days:
                cap_high = mid_cap - 1
                
            
        return lowest_cap
        

s = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5


result = s.shipWithinDays(weights=weights, days=days)
print(result)

