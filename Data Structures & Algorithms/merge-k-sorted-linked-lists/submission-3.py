# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0: return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                x = lists[i]
                y = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.merge(x, y))
            lists = mergedLists
        
        return lists[0]


    def merge(self, x, y):
        dummy = curr =  ListNode()
        while x and y:
            if x.val < y.val:
                curr.next = x
                x = x.next
            else:
                curr.next = y
                y = y.next

            curr = curr.next
        
        if not y:
            curr.next = x    
        if not x:
            curr.next = y
        
        return dummy.next


