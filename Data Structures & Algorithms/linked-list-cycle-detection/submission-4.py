# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast is not None:
            if fast.next is None or fast.next.next is None: return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False