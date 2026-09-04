"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        missing = defaultdict(list)
        new = {}
        newHead = None
        prevNew = None
        curr = head

        while curr:
            n = Node(curr.val, None, None)
            new[curr] = n
            if prevNew:
                prevNew.next = n

            if not newHead: newHead = n

            if curr.random is None:
                n.random = None
            elif curr.random in new:
                n.random = new[curr.random]
            else:
                missing[curr.random].append(n)
            
            if curr in missing:
                for i in missing[curr]:
                    i.random = n
                
                del missing[curr]

            prevNew = n
            curr = curr.next
        
        return newHead