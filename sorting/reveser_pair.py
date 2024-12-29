class Solution:
    def reversePairs(self, nums) -> int:
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst, 0  # Return the list itself and 0 inversions

            mid = len(lst) // 2
            left_half, left_inv = merge_sort(lst[:mid])
            right_half, right_inv = merge_sort(lst[mid:])
            merged_list, cross_inv = merge(left_half, right_half)

            total_inv = left_inv + right_inv + cross_inv
            return merged_list, total_inv

        def merge(left, right):
            merged = []
            count = 0
            i = j = 0

            # Count reverse pairs
            temp_j = 0
            for i in range(len(left)):
                while temp_j < len(right) and left[i] > 2 * right[temp_j]:
                    temp_j += 1
                count += temp_j

            # Reset pointers for merging
            i = j = 0

            # Merge the two sorted lists
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, total_reverse_pairs = merge_sort(nums)
        return total_reverse_pairs
