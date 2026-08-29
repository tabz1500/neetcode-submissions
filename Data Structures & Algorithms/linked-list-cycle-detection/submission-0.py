# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        nodes = {}
        idx = 0

        while curr:
            if curr in nodes:
                return True
            nodes[curr] = idx
            curr = curr.next
            idx += 1
        
        return False