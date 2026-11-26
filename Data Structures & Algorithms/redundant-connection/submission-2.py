class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def hasCycle(node, prev):
            if node in seen:
                return True

            seen.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if hasCycle(neighbor, node):
                    return True

            return False
        
        
        
        adjList = defaultdict(set)

        for edge in edges:
            e0 = edge[0]
            e1 = edge[1]
            adjList[e0].add(e1)
            adjList[e1].add(e0)

        for edge in reversed(edges):
            e0 = edge[0]
            e1 = edge[1]
            adjList[e0].remove(e1)
            adjList[e1].remove(e0)

            seen = set()

            if not hasCycle(e0, -1) and len(seen) == len(adjList):
                return edge

            adjList[e0].add(e1)
            adjList[e1].add(e0)



