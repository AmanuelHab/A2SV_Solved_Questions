# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        prev = None
        curr = head
        nxt = head.next
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        head = curr
        
        # Remove the following lesser value nodes
        while curr and curr.next:
            if curr.next.val < curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # Reverse the list again
        prev = None
        curr = head
        nxt = head.next
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        head = curr
        return head