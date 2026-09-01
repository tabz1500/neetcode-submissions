# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        res = curr = nodes[0]
        l = 1
        r = len(nodes) - 1
        count = 1

        while l <= r:
            if count % 2 == 0:
                curr.next = nodes[l]
                curr = curr.next
                l += 1
            else:
                curr.next = nodes[r]
                curr = curr.next
                r -= 1
            count += 1
        
        curr.next = None
        
        head = res