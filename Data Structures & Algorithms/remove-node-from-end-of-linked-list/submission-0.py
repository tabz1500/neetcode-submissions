# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        sidx = 0
        fast = slow.next
        if fast:
            count = 2
        else:
            count = 1
        
        while fast:
            fast = fast.next
            if fast:
                count += 1
                fast = fast.next
                if fast:
                    count += 1
            slow = slow.next
            sidx += 1

        index = count - n
        if sidx < index:
            curr = slow
            i = sidx
        else:
            curr = head
            i = 0
        
        prev = None

        while curr and i != index:
            prev = curr
            curr = curr.next
            i += 1
        
        if prev: prev.next = curr.next
        else:
            head = curr.next
        curr.next = None

        return head

