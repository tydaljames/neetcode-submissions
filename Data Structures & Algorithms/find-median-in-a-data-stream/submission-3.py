class MedianFinder:
    def __init__(self):
        self.tophalf = [float("inf")]
        self.bothalf = [float("-inf")]
        self.median = None

        heapq.heapify(self.tophalf)
        heapq.heapify_max(self.bothalf)

    def addNum(self, num: int) -> None:
        print = lambda *args, **kwargs: None

        if self.median != None:
            print("took median")
            heapq.heappush(self.tophalf, max(self.median, num))
            heapq.heappush_max(self.bothalf, min(self.median, num))
            self.median = None
            return

        if num > self.tophalf[0]:
            print("path1")

            heapq.heappush(self.tophalf, num)
        else:
            print("path2")

            heapq.heappush_max(self.bothalf, num)
        
        if len(self.tophalf) > len(self.bothalf):
            print("path3")

            self.median = heapq.heappop(self.tophalf)
        else:
            print("path4")

            self.median = heapq.heappop_max(self.bothalf)

        print(num, self.median, self.tophalf, self.bothalf)




    # nums
    # tophalf = [inf]
    # bothalf = [-inf]

    def findMedian(self) -> float:
        if self.median != None:
            return self.median

        return (self.tophalf[0] + self.bothalf[0]) / 2


