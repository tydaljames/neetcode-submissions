class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0 for _ in range(26)]

        for task in tasks:
            counts[ord(task) - ord("A")] += 1

        heapq.heapify_max(counts)

        firstCount = heapq.heappop_max(counts)

        empty = (firstCount - 1) * n
        cycles = empty + firstCount

        while counts:
            count = heapq.heappop_max(counts)
            if count == firstCount and empty > 0:
                cycles += 1
                empty -= (firstCount - 1)
            

            else:
                empty -= count

        
        return cycles - (empty if empty < 0 else 0)