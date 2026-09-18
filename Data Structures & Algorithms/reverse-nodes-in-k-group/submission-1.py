# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        preHead = tail = dummy
        count = 0
        while tail:
            if count < k:
                tail = tail.next
                count += 1
            else:
                head = preHead.next
                seam = tail.next
                self.reverse(head, tail)
                preHead.next = tail
                head.next = seam
                preHead = tail = head
                count = 0
        
        return dummy.next

    def reverse(self, head, tail):
        if head == tail:
            return head
        else:
            x = self.reverse(head.next, tail)
            x.next = head
            return x.next
