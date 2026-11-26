class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        n = len(nums)

        def part(i, sum1):
            if sum1 == half:
                return True
            if sum1 > half or i >= n:
                return False
            
            return part(i + 1, sum1 + nums[i]) or part(i + 1, sum1)

        return part(0, 0)