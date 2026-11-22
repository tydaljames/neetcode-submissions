class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def checkNodes(node, prev):
            if node in seen:
                return False
            
            seen.add(node)

            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue

                if not checkNodes(neighbor, node):
                    return False

            return True

        adjList = [[] for _ in range(n)]

        for edge in edges:
            start = edge[0]
            stop = edge[1]

            adjList[start].append(stop)
            adjList[stop].append(start)

        seen = set()
        if not checkNodes(0, -1):
            return False

        return len(seen) == n

