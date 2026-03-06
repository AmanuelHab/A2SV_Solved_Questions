# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        first_even = head.next
        even = first_even
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
            if even.next:
                even.next = even.next.next
                even = even.next
        odd.next = first_even
        return head 