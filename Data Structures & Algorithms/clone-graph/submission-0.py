"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    seen = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.seen:
            return self.seen[node]

        new = Node(node.val)
        print(node.val, new.val)

        self.seen[node] = new

        
        for neighbor in node.neighbors:
            newNeighbor = self.cloneGraph(neighbor)
            if newNeighbor:
                new.neighbors.append(newNeighbor)




        return new