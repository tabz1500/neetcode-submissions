# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resHead = None
        curr = head
        while curr:
            oldNext = curr.next
            curr.next = resHead
            resHead = curr
            curr = oldNext
        
        return resHead

        