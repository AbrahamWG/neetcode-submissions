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
        # random points to the index node
        # hashmap k: node, v: random node index
        # need to map each original node to its new copy

        # key: new copy node, value: all new nodes who points to this node
        d = {}
        curr = head

        # populate the dict
        while curr:
            if curr not in d:
                d[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            # value link to value
            d[curr].next = d.get(curr.next) #get will safely return None 
            d[curr].random = d.get(curr.random)
            curr = curr.next

        return d.get(head)
        
            