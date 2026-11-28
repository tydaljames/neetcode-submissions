class MedianFinder:
    def __init__(self):
        self.tophalf = [float("inf")]
        self.bothalf = [float("-inf")]
        self.median = None

        heapq.heapify(self.tophalf)
        heapq.heapify_max(self.bothalf)

    def addNum(self, num: int) -> None:
        if self.median != None:
            heapq.heappush(self.tophalf, max(self.median, num))
            heapq.heappush_max(self.bothalf, min(self.median, num))
            self.median = None
            return

        if num > self.tophalf[0]:
            heapq.heappush(self.tophalf, num)
        else:
            heapq.heappush_max(self.bothalf, num)
        
        if len(self.tophalf) > len(self.bothalf):
            self.median = heapq.heappop(self.tophalf)
        else:
            self.median = heapq.heappop_max(self.bothalf)

    def findMedian(self) -> float:
        if self.median != None:
            return self.median

        return (self.tophalf[0] + self.bothalf[0]) / 2


