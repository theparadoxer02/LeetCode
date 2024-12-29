def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        cut2 = 1
        cut1 = ((len1 + len2) // 2) - cut2

        print(cut1, cut2)

        l1 = nums1[cut1 - 1]
        l2 = nums2[cut2 - 2]
        r1 = nums1[cut1]
        r2 = nums2[cut2]

        # print(l1, l2, r1, r2, cut1, cut2)
        while not(l1 <= r2 and l2 <= r1):
            print(cut1, cut2)
            if l1 > r2:
                cut1 -= 1
                cut2 += 1

            elif l2 > r1:
                cut2 += 1
                cut1 -= 1


num1 = [1, 3, 4, 7, 10, 11]
num2 = [2, 3, 6, 15]

abc = findMedianSortedArrays(nums1=num1, nums2=num2)
print(abc)
