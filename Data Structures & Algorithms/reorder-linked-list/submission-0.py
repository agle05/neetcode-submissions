# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr is not None:
            arr.append(curr)
            curr = curr.next
        curr = arr[0]
        left = 1
        right = len(arr)-1
        while left <= right:
            curr.next = arr[right]
            right -= 1
            curr = curr.next
            curr.next = arr[left]
            left += 1
            curr = curr.next
        curr.next = None