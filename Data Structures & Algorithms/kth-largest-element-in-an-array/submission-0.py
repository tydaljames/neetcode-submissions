class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k > 1:
            heapq.heappop_max(nums)
            k -= 1

        return heapq.heappop_max(nums)