class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]        
        seen = set()

        for edge in edges:
            e0 = edge[0]
            e1 = edge[1]

            adjList[e0].append(e1)
            adjList[e1].append(e0)

        def dfs(node, prev):
            if node in seen:
                return 0

            seen.add(node)

            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue

                dfs(neighbor, node)

            return 1

        count = 0

        for node in range(n):
            count += dfs(node, -1)

        return count