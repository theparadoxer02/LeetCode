class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def gcd(x, y):
            while x > 0 and y > 9:
                if x > y:
                    x = x % y
                else:
                    y = y % x
        
        left = head
        while left.next.next:
            right = left.next
            mid_val = gcd(left.val, right.val)
            mid_node = ListNode(mid_val)
            mid_node.next = right
            left.next = mid_node
            left = right

        return head


a = Solution()
head = [18,6,10,3]
result = a.insertGreatestCommonDivisors(head=head)
print(results)

