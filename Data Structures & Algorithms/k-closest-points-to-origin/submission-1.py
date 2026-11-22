class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x, y):
            return math.sqrt((x**2) + (y**2))

        minDist = []

        for point in points:
            dist = getDist(point[0], point[1])
            minDist.append([dist, point])


        heapq.heapify(minDist)
        res = []

        while k > 0:
            res.append(heapq.heappop(minDist)[1])
            k -= 1

        # minDist.sort

        # print(minDist)
        # res = []
        # for dist in minDist[:k]:
        #     res.append(dist[1])

        return res
