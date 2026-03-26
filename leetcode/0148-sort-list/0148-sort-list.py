# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # mergesort method
        if not head:
            return None
        slow = head
        fast = head.next
        if not fast:
            return head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_half = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_half)

        curr = dummy = ListNode(0)
        l = left
        r = right
        while l and r:
            if l.val > r.val:
                curr.next = r
                curr = curr.next
                r = r.next
            else:
                curr.next = l 
                curr = curr.next
                l = l.next
        while l:
            curr.next = l
            curr = curr.next
            l = l.next
        while r:
            curr.next = r
            curr = curr.next
            r = r.next
        return dummy.next