# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head

        while s and f:
            s = s.next
            f = f.next
            if f:
                f = f.next
            else:
                return False

            if s == f:
                return True
        
        return False