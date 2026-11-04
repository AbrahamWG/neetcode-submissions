class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        count = 0
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for val in graph[i]:
                if val not in visited:
                    dfs(val)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        # input n = 5, edges = [[0,1],[1,2],[3,4]]
        # dfs(0, [])
            # visiting = [0]
            # visited = [0]
            # dfs(1, [0])
                # visitng = [0, 1]
                # visited = [0, 1]
                # dfs(2, [0, 1])
                    # visiting = [0, 1, 2]
                    # visited = [0, 1, 2]
        # count = 1, visited = [0, 1, 2]
        # i = 1, skip
        # i = 2, skip
        # i = 3, dfs(3, [])
            # visiting = [3]
            # visited = [0, 1, 2, 3]
            # dfs(3, [3])
                # visiting [3, 4]
                # visited = [0, 1, 2, 3, 4]
        # count = 2
        # i = 4, skip
        # return 2
