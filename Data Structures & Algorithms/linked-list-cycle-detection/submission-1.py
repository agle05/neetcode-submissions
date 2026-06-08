# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        if curr is None:
            return False
        while count <= 1000:
            if curr.next is None:
                return False
            else:
                curr = curr.next
                count += 1

        return True