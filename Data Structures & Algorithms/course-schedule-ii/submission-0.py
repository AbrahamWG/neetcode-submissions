class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs approach
        # build adjacency list mapping first
        # iterate from course 0 asc
        # if course in visiting means loop, return []
        # if dfs call done, put course in visited

        courses = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            courses[prereq[0]].append(prereq[1])
        
        visited = set()
        visiting = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order
        
