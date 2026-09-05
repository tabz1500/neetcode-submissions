# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        total = 0
        place = 1

        while curr1 and curr2:
            load = (curr1.val * place) + (curr2.val * place)
            total += load
            place *= 10
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            total += (curr1.val * place)
            place *= 10
            curr1 = curr1.next
        
        while curr2:
            total += (curr2.val * place)
            place *= 10
            curr2 = curr2.next
        
        res = node = ListNode(0, None)
        if total == 0: return res
        while total > 0:
            val = total % 10
            node.next = ListNode(val, None)
            total = total // 10
            node = node.next
        
        return res.next
