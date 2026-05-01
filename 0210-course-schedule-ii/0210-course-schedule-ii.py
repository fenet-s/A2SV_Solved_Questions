class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for course , pre in prerequisites:
            adjlist[pre].append(course)

        stack = []
        visited = set()
        tracker = set()
        self.cycle = False

        def dfs(node, visited, tracker,stack):
            visited.add(node)
            tracker.add(node)
            for nx in adjlist[node]:
                if nx in tracker:
                    self.cycle = True

                if nx not in visited:
                    dfs(nx,visited,tracker,stack)
            tracker.remove(node)
            stack.append(node)
        
        for node in range(numCourses):
            if node not in visited:
                dfs(node, visited, tracker, stack)
        if self.cycle:
            return []
        return stack[::-1]

