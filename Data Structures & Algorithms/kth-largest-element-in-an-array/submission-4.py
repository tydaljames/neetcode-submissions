class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            pivot = nums[right]
            p = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[right] = pivot, nums[p]

            if p > k:
                return quickSelect(left, p - 1)
            elif p < k:
                return quickSelect(p + 1, right)
            return nums[p]

        return quickSelect(0, len(nums) - 1)