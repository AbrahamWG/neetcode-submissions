class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # every node starts as its own group leader
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            # walk up to the root, flattening the path as we go
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                # already connected, so this edge makes a cycle
                return False
            # attach the smaller tree under the bigger one
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            rank[root_a] += rank[root_b]
            return True

        # go in input order, so the first edge that fails is the last valid answer
        for a, b in edges:
            if not union(a, b):
                return [a, b]