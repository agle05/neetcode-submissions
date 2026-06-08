# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None: return None

        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        next: Optional[ListNode] = head.next
        curr.next: Optional[ListNode] = prev
        prev = curr
        curr = next

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
