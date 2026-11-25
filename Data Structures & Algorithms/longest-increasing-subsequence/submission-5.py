class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1 for _ in range(n)]

        def dfs(i, prev):
            # print("start", i, prev, memo)
            if i >= n or nums[i] <= prev:
                return 0

            if memo[i] != -1:
                return memo[i]

            num = nums[i]
            
            localMax = 1
            for j in range(i, n):
                localMax = max(localMax, dfs(j + 1, num) + 1)

            memo[i] = localMax
            return memo[i]


        fmax = 1
        for i in range(n):
            fmax = max(dfs(i, -1e9), fmax)

        return fmax

        