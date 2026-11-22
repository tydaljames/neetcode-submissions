class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topK = []
        self.rest = nums.copy()
        self.k = k

        heapq.heapify_max(self.rest)

        while k > 0:
            if not self.rest:
                self.topK.append(float('-inf'))
            else:
                self.topK.append(heapq.heappop_max(self.rest))
            k -= 1

        heapq.heapify(self.topK)

        # print(self.rest, self.topK)

        

    def add(self, val: int) -> int:
        lowestHi = heapq.heappop(self.topK)

        heapq.heappush(self.topK, max(lowestHi, val))
        heapq.heappush_max(self.rest, min(lowestHi, val))

        return self.topK[0]