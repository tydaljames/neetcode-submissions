class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
  
        if n <= 3:
            return max(nums)
        dp1 = [0 for _ in range(n)]
        dp = [0 for _ in range(n + 1)]

        for i in range(2, n - 1):
            dp1[0] = nums[0]
            dp1[1] = max(nums[0], nums[1])
            take = dp1[i - 2] + nums[i]
            skip = dp1[i - 1]

            print(i, dp1, take, skip)
            dp1[i] = max(take, skip)

        for i in range(3, n):
            dp[1] = nums[1]
            dp[2] = max(nums[1], nums[2])
            take = dp[i - 2] + nums[i]
            skip = dp[i - 1]

            dp[i] = max(take, skip)
        
        return max(dp1[n - 2], dp[n - 1])
