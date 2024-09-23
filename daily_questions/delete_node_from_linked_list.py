class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val in [nums]:
                if curr.next == head:
                    head = curr.next.next
                curr.next = curr.next.next
            curr = curr.next

nums = [1, 2, 3]
head = [1, 2, 3, 4, 5]

s = Solution()
result = s.modifiedList(nums=nums, head=head)
print(result)
