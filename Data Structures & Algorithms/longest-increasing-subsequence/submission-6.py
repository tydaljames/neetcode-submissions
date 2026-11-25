class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n + 1)]

        for left in range(n - 1, -1, -1):
            for right in range(left + 1, n):
                if nums[right] > nums[left]:
                    dp[left] = max(dp[left], dp[right] + 1)

        return max(dp)




        return -1
