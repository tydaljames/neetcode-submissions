class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x, y):
            return (x**2) + (y**2)

        
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
