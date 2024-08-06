class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)

        if m * k > n:
            return -1


        def get_num_of_bouquets(mid):
            num_of_bouquets = 0
            count = 0

            for day in bloomDay:
                # If the flower is bloomed, add to the set. Else reset the count.
                if day <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    num_of_bouquets += 1
                    count = 0

            return num_of_bouquets


        def binary_search(low, high):
            if low == high:
                return low
            
            mid = (low + high ) // 2

            result = get_num_of_bouquets(mid)

            if result < m:
                low = mid + 1
            else:
                high = mid - 1
            
            return binary_search(low, high)

        end_range = max(bloomDay)
        return binary_search(0, end_range)