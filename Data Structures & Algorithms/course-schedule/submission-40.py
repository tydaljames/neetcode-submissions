class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]

        for p in prerequisites:
            start = p[1]
            end = p[0]

            adjList[start].append(end)


        def dfs(node, seen):
            if node in seen:
                return False
            if node in valid:
                return True
            seen.add(node)

            for neighbor in adjList[node]:
                
                if not dfs(neighbor, seen):
                    return False
                
            seen.remove(node)
            valid.add(node)
            return True

        valid = set()
        for p in range(numCourses):
            if not dfs(p, set()):
                return False


        return True
