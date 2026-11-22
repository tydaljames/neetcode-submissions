class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjList = {i:[] for i in range(numCourses)}
        adjList = [[] for _ in range(numCourses)]

        for p in prerequisites:
            start = p[0] 
            end = p[1]

            adjList[start].append(end)

        result = []


        def dfs(node, seen):
            if node in seen:
                return False
            if not adjList[node]:
                return True

            seen.add(node)
            for neighbor in reversed(adjList[node]):
                if not dfs(neighbor, seen):
                    return False
                adjList[node].pop()


            seen.remove(node)
            result.append(node)
            return True

        for course, neighbors in enumerate(adjList):
            if not neighbors:
                result.append(course)

        for course in range(numCourses):
            if not dfs(course, set()):
                return []

        return result