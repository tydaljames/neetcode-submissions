class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [[0, i] for i in range(26)]
        heap = []
        flex = []

        for task in tasks:
            counts[ord(task) - ord("A")][0] += 1

        heapq.heapify_max(counts)
        heapq.heapify_max(flex)


        firstCount = heapq.heappop_max(counts)[0]

        empty = (firstCount - 1) * n
        cycles = empty + firstCount

        while counts:
            count = heapq.heappop_max(counts)[0]
            if count == firstCount:
                if empty == 0:
                    cycles += firstCount
                else:
                    cycles += 1
                    empty -= (firstCount - 1)
            

            else:
                empty -= count



        
        return cycles - (empty if empty < 0 else 0)