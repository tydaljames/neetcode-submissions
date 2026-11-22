class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1 for _ in range(n)]

        def dfs(i):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]

            take = dfs(i + 2) + nums[i]
            skip = dfs(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return dfs(0)