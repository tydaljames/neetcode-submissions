class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x, y):
            return (x**2) + (y**2)

        
        points.sort(key=lambda p: getDist(p[0], p[1]))
        return points[:k]
