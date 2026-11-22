class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjMatrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        adjList = [[] for _ in range(numCourses)]
        # adjList = []

        for p in prerequisites:
            start = p[1]
            end = p[0]

            adjList[start].append(end)


        # print(adjList)

        def dfs(node, seen):
            # print("dfs at node:", node)
            if node in valid:
                return True
            seen.add(node)

            for neighbor in adjList[node]:
                if neighbor in seen:
                    # print("Found cycle")  
                    return False
                if not dfs(neighbor, seen):
                    return False
                
            seen.remove(node)
            valid.add(node)
            return True

        # seen = set()
        valid = set()
        for p in range(numCourses):
            if p in valid:
                continue
            # print("Starting", p)
            if not dfs(p, set()):
                return False


        return True
