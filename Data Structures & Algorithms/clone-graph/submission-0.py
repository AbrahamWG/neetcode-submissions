"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {} # keep track of cloned nodes

        def dfs(curr):
            if not curr: # if reach an end or just None
                return None
            if curr in cloned: # return the cloned version from cloned
                return cloned[curr]
                
            clone = Node(curr.val, [])
            cloned[curr] = clone
            clone.neighbors = [dfs(n) for n in curr.neighbors]
            
            return clone
        
        return dfs(node)