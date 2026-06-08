# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp: Optional[ListNode] = ListNode(0)
        curr: Optional[ListNode] = temp

        while list1 is not None and list2 is not None:
            if list2.val <= list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        curr.next = list1 or list2
        
        return temp.next
