class Node:
    def __init__(self, key, val):
        # each node has 2 pointers, prev and next
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    # hashmap and doubly linkedlist
    # hashmap to access key value in O(1)
    # double linkedlist to move nodes from MRU to LRU in O(1)

    # left node: LRU
    # right node: MRU
    # initial state: None <= left <=> right => None
    # put(1, 1): left <=> n1 <=> right  
    # put(2, 2): left <=> n1 <=> n2 <=> right
    # get(1, 1): left <=> n2 <=> n1 <=> right
    # put(3, 3): left <=> n1 <=> n3 <=> right  (remove n2, shift n1, insert n3)


    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # value is a pointer

        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # helper functions
    def insert(self, node):
        """
        put the node in the middle: 
        left <=> n1 <=> right
        left <=> n1 <=> n2 <=> right
        """
        prev = self.right.prev # prev is the node just before right
        nxt = self.right # set the curr node's next to right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        """
        take the curr node's prev and next
        to skip curr node, set the prev's next to curr node's next
        set node's next.prev to be node.prev
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        """ 
        if key exist in cache, we have to move it to MRU
        remove that value node first from the linkedlist
        then insert it back again to the left of right dummy node
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)