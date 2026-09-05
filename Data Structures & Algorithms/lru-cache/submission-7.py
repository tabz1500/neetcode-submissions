class ListNode:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.cache = {}
        # left is the least used
        self.left = ListNode(0,0)
        # right is most used
        self.right = ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Insert right before self.right
        most = self.right.prev
        most.next = node
        node.prev = most
        node.next = self.right  # Fixed: explicitly point to self.right
        self.right.prev = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.count == self.cap:
                # Evict least recently used node
                least = self.left.next
                self.left.next = least.next
                least.next.prev = self.left
                del self.cache[least.key]
            else:
                self.count += 1
            
            node = ListNode(key, value)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.value = value  # Fixed: update node value on cache hit
            node.prev.next = node.next
            node.next.prev = node.prev
        
        # Insert right before self.right
        most = self.right.prev
        most.next = node
        node.prev = most
        node.next = self.right
        self.right.prev = node