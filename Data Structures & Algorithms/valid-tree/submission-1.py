class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # use dfs
        # build adj list
        # check if there are separate trees and cycle, ret false

        graph = {i: [] for i in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = set()
        def dfs(parent, current):
            if current in visited:
                return False
            visited.add(current)
            for child in graph.get(current):
                if child == parent:
                    continue
                if not dfs(current, child):
                    return False
            return True
    
        return dfs(None, 0) and len(visited) == n

        # trace: n = 5, edges = [[0,1],[2,0],[3,0],[1,4]]
        # 0: 1, 2, 3
        # 1: 0, 4
        # 2: 0
        # 3: 0
        # 4: 1